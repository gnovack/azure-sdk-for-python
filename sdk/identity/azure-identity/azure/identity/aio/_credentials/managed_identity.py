# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os
from typing import TYPE_CHECKING

from azure.core.credentials import AccessToken
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
from azure.core.pipeline.policies import AsyncRetryPolicy

from azure.identity._credentials.managed_identity import _ManagedIdentityBase
from .._authn_client import AsyncAuthnClient
from ..._constants import Endpoints, EnvironmentVariables

if TYPE_CHECKING:
    from typing import Any, Optional
    from azure.core.configuration import Configuration


class ManagedIdentityCredential(object):
    """Authenticates with an Azure managed identity in any hosting environment which supports managed identities.

    See the Azure Active Directory documentation for more information about managed identities:
    https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview

    :keyword str client_id: ID of a user-assigned identity. Leave unspecified to use a system-assigned identity.
    """

    def __new__(cls, *args, **kwargs):
        if os.environ.get(EnvironmentVariables.MSI_ENDPOINT):
            return MsiCredential(*args, **kwargs)
        return ImdsCredential(*args, **kwargs)

    # the below methods are never called, because ManagedIdentityCredential can't be instantiated;
    # they exist so tooling gets accurate signatures for Imds- and MsiCredential
    def __init__(self, **kwargs: "Any") -> None:
        pass

    async def get_token(self, *scopes: str, **kwargs: "Any") -> "AccessToken":  # pylint:disable=unused-argument
        """Asynchronously request an access token for `scopes`.

        .. note:: This method is called by Azure SDK clients. It isn't intended for use in application code.

        :param str scopes: desired scopes for the token
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.core.exceptions.ClientAuthenticationError:
        """
        return AccessToken()


class _AsyncManagedIdentityBase(_ManagedIdentityBase):
    def __init__(self, endpoint: str, **kwargs: "Any") -> None:
        super().__init__(endpoint=endpoint, client_cls=AsyncAuthnClient, **kwargs)

    @staticmethod
    def _create_config(**kwargs: "Any") -> "Configuration":
        """Build a default configuration for the credential's HTTP pipeline."""
        return _ManagedIdentityBase._create_config(retry_policy=AsyncRetryPolicy, **kwargs)


class ImdsCredential(_AsyncManagedIdentityBase):
    """Asynchronously authenticates with a managed identity via the IMDS endpoint.

    :keyword str client_id: ID of a user-assigned identity. Leave unspecified to use a system-assigned identity.
    """

    def __init__(self, **kwargs: "Any") -> None:
        super().__init__(endpoint=Endpoints.IMDS, **kwargs)
        self._endpoint_available = None  # type: Optional[bool]

    async def get_token(self, *scopes: str, **kwargs: "Any") -> AccessToken:  # pylint:disable=unused-argument
        """Asynchronously request an access token for `scopes`.

        :param str scopes: desired scopes for the token
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.core.exceptions.ClientAuthenticationError:
        """
        if self._endpoint_available is None:
            # Lacking another way to determine whether the IMDS endpoint is listening,
            # we send a request it would immediately reject (missing a required header),
            # setting a short timeout.
            try:
                await self._client.request_token(scopes, method="GET", connection_timeout=0.3, retry_total=0)
                self._endpoint_available = True
            except (ClientAuthenticationError, HttpResponseError):
                # received a response a pipeline policy choked on (HttpResponseError)
                # or that couldn't be deserialized by AuthnClient (AuthenticationError)
                self._endpoint_available = True
            except Exception:  # pylint:disable=broad-except
                # if anything else was raised, assume the endpoint is unavailable
                self._endpoint_available = False

        if not self._endpoint_available:
            raise ClientAuthenticationError(message="IMDS endpoint unavailable")

        if len(scopes) != 1:
            raise ValueError("this credential supports one scope per request")

        token = self._client.get_cached_token(scopes)
        if not token:
            resource = scopes[0]
            if resource.endswith("/.default"):
                resource = resource[: -len("/.default")]
            params = {"api-version": "2018-02-01", "resource": resource}
            if self._client_id:
                params["client_id"] = self._client_id
            token = await self._client.request_token(scopes, method="GET", params=params)
        return token


class MsiCredential(_AsyncManagedIdentityBase):
    """Authenticates via the MSI endpoint in an App Service or Cloud Shell environment.

    :keyword str client_id: ID of a user-assigned identity. Leave unspecified to use a system-assigned identity.
    """

    def __init__(self, **kwargs: "Any") -> None:
        self._endpoint = os.environ.get(EnvironmentVariables.MSI_ENDPOINT)
        if self._endpoint:
            super().__init__(endpoint=self._endpoint, **kwargs)

    async def get_token(self, *scopes: str, **kwargs: "Any") -> AccessToken:  # pylint:disable=unused-argument
        """Asynchronously request an access token for `scopes`.

        :param str scopes: desired scopes for the token
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.core.exceptions.ClientAuthenticationError:
        """
        if not self._endpoint:
            raise ClientAuthenticationError(message="MSI endpoint unavailable")

        if len(scopes) != 1:
            raise ValueError("this credential supports only one scope per request")

        token = self._client.get_cached_token(scopes)
        if not token:
            resource = scopes[0]
            if resource.endswith("/.default"):
                resource = resource[: -len("/.default")]

            secret = os.environ.get(EnvironmentVariables.MSI_SECRET)
            if secret:
                # MSI_ENDPOINT and MSI_SECRET set -> App Service
                token = await self._request_app_service_token(scopes=scopes, resource=resource, secret=secret)
            else:
                # only MSI_ENDPOINT set -> legacy-style MSI (Cloud Shell)
                token = await self._request_legacy_token(scopes=scopes, resource=resource)
        return token

    async def _request_app_service_token(self, scopes, resource, secret):
        params = {"api-version": "2017-09-01", "resource": resource}
        if self._client_id:
            params["clientid"] = self._client_id
        return await self._client.request_token(scopes, method="GET", headers={"secret": secret}, params=params)

    async def _request_legacy_token(self, scopes, resource):
        form_data = {"resource": resource}
        if self._client_id:
            form_data["client_id"] = self._client_id
        return await self._client.request_token(scopes, method="POST", form_data=form_data)
