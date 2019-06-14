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

from .service_resource_properties_base import ServiceResourcePropertiesBase


class ServiceResourceProperties(ServiceResourcePropertiesBase):
    """The service resource properties.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: StatefulServiceProperties, StatelessServiceProperties

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme: A list that describes the correlation of the
     service with other services.
    :type correlation_scheme:
     list[~azure.mgmt.servicefabric.models.ServiceCorrelationDescription]
    :param service_load_metrics: The service load metrics is given as an array
     of ServiceLoadMetricDescription objects.
    :type service_load_metrics:
     list[~azure.mgmt.servicefabric.models.ServiceLoadMetricDescription]
    :param service_placement_policies: A list that describes the correlation
     of the service with other services.
    :type service_placement_policies:
     list[~azure.mgmt.servicefabric.models.ServicePlacementPolicyDescription]
    :param default_move_cost: Specifies the move cost for the service.
     Possible values include: 'Zero', 'Low', 'Medium', 'High'
    :type default_move_cost: str or ~azure.mgmt.servicefabric.models.MoveCost
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response
    :vartype provisioning_state: str
    :param service_type_name: The name of the service type
    :type service_type_name: str
    :param partition_description: Describes how the service is partitioned.
    :type partition_description:
     ~azure.mgmt.servicefabric.models.PartitionSchemeDescription
    :param service_package_activation_mode: The activation Mode of the service
     package. Possible values include: 'SharedProcess', 'ExclusiveProcess'
    :type service_package_activation_mode: str or
     ~azure.mgmt.servicefabric.models.ArmServicePackageActivationMode
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'placement_constraints': {'key': 'placementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'correlationScheme', 'type': '[ServiceCorrelationDescription]'},
        'service_load_metrics': {'key': 'serviceLoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'servicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'defaultMoveCost', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'service_type_name': {'key': 'serviceTypeName', 'type': 'str'},
        'partition_description': {'key': 'partitionDescription', 'type': 'PartitionSchemeDescription'},
        'service_package_activation_mode': {'key': 'servicePackageActivationMode', 'type': 'str'},
        'service_kind': {'key': 'serviceKind', 'type': 'str'},
    }

    _subtype_map = {
        'service_kind': {'Stateful': 'StatefulServiceProperties', 'Stateless': 'StatelessServiceProperties'}
    }

    def __init__(self, **kwargs):
        super(ServiceResourceProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.service_type_name = kwargs.get('service_type_name', None)
        self.partition_description = kwargs.get('partition_description', None)
        self.service_package_activation_mode = kwargs.get('service_package_activation_mode', None)
        self.service_kind = None
        self.service_kind = 'ServiceResourceProperties'
