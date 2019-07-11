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


class IoTSecurityDeviceAlert(Model):
    """Statistic information about the number of alerts per alert type during the
    last period.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar alert_display_name: Display name of the alert
    :vartype alert_display_name: str
    :ivar reported_severity: Estimated severity of this alert. Possible values
     include: 'Informational', 'Low', 'Medium', 'High'
    :vartype reported_severity: str or
     ~azure.mgmt.security.models.ReportedSeverity
    :ivar alerts_count: the number of alerts raised for this alert type
    :vartype alerts_count: int
    """

    _validation = {
        'alert_display_name': {'readonly': True},
        'reported_severity': {'readonly': True},
        'alerts_count': {'readonly': True},
    }

    _attribute_map = {
        'alert_display_name': {'key': 'alertDisplayName', 'type': 'str'},
        'reported_severity': {'key': 'reportedSeverity', 'type': 'str'},
        'alerts_count': {'key': 'alertsCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(IoTSecurityDeviceAlert, self).__init__(**kwargs)
        self.alert_display_name = None
        self.reported_severity = None
        self.alerts_count = None
