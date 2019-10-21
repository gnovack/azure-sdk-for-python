# Stubs for aio._azure_configuration_client_async (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .._azure_appconfiguration_credential import AppConfigConnectionStringCredential
from .._azure_appconfiguration_error import ResourceReadOnlyError
from .._azure_appconfiguration_requests import AppConfigRequestsCredentialsPolicy
from .._generated.aio import AzureAppConfiguration
from .._generated.aio._configuration_async import AzureAppConfigurationConfiguration
from .._generated.models import ErrorException, KeyValue
from .._models import ConfigurationSetting
from .._user_agent import USER_AGENT
from .._utils import escape_and_tostr, get_endpoint_from_connection_string, prep_if_match, prep_if_none_match
from azure.core import MatchConditions
from typing import Any

class AzureAppConfigurationClient:
    config: Any = ...
    def __init__(self, base_url: str, credential: AppConfigConnectionStringCredential, **kwargs: Any) -> None: ...
    @classmethod
    def from_connection_string(cls: Any, connection_string: str, **kwargs: Any) -> AzureAppConfigurationClient: ...
    def list_configuration_settings(self, keys: list=..., labels: list=..., **kwargs: dict) -> azure.core.paging.ItemPaged[ConfigurationSetting]: ...
    async def get_configuration_setting(self, key: str, label: str=..., etag: str=..., match_condition: MatchConditions=..., **kwargs: dict) -> ConfigurationSetting: ...
    async def add_configuration_setting(self, configuration_setting: ConfigurationSetting, **kwargs: dict) -> ConfigurationSetting: ...
    async def set_configuration_setting(self, configuration_setting: ConfigurationSetting, match_condition: MatchConditions=..., **kwargs: dict) -> ConfigurationSetting: ...
    async def delete_configuration_setting(self, key: str, label: str=..., etag: str=..., match_condition: MatchConditions=..., **kwargs: dict) -> ConfigurationSetting: ...
    def list_revisions(self, keys: list=..., labels: list=..., **kwargs: dict) -> azure.core.paging.ItemPaged[ConfigurationSetting]: ...
    async def set_read_only(self, configuration_setting: ConfigurationSetting, **kwargs: dict) -> ConfigurationSetting: ...
    async def clear_read_only(self, configuration_setting: ConfigurationSetting, **kwargs: dict) -> ConfigurationSetting: ...
