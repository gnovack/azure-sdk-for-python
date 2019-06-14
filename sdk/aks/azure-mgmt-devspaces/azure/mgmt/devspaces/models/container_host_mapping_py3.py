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


class ContainerHostMapping(Model):
    """Container host mapping object specifying the Container host resource ID and
    its associated Controller resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param container_host_resource_id: ARM ID of the Container Host resource
    :type container_host_resource_id: str
    :ivar mapped_controller_resource_id: ARM ID of the mapped Controller
     resource
    :vartype mapped_controller_resource_id: str
    """

    _validation = {
        'mapped_controller_resource_id': {'readonly': True},
    }

    _attribute_map = {
        'container_host_resource_id': {'key': 'containerHostResourceId', 'type': 'str'},
        'mapped_controller_resource_id': {'key': 'mappedControllerResourceId', 'type': 'str'},
    }

    def __init__(self, *, container_host_resource_id: str=None, **kwargs) -> None:
        super(ContainerHostMapping, self).__init__(**kwargs)
        self.container_host_resource_id = container_host_resource_id
        self.mapped_controller_resource_id = None
