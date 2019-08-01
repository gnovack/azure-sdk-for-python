# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateGatewaySettingsParameters(Model):
    """The update gateway settings request parameters.

    :param is_credential_enabled: Indicates whether or not the gateway
     settings based authorization is enabled. Default value: True .
    :type is_credential_enabled: bool
    :param user_name: The gateway settings user name.
    :type user_name: str
    :param password: The gateway settings user password.
    :type password: str
    """

    _attribute_map = {
        'is_credential_enabled': {'key': 'restAuthCredential\\.isEnabled', 'type': 'bool'},
        'user_name': {'key': 'restAuthCredential\\.username', 'type': 'str'},
        'password': {'key': 'restAuthCredential\\.password', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UpdateGatewaySettingsParameters, self).__init__(**kwargs)
        self.is_credential_enabled = kwargs.get('is_credential_enabled', True)
        self.user_name = kwargs.get('user_name', None)
        self.password = kwargs.get('password', None)