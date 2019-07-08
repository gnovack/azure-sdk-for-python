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


class AnomalyDetectOnTimestampRequest(Model):
    """AnomalyDetectOnTimestampRequest.

    All required parameters must be populated in order to send to Azure.

    :param timestamp: Required. Timestamp of a data point
    :type timestamp: datetime
    :param period: Optional argument, periodic value of a time series. If the
     value is null or does not present, the API will determine the period
     automatically.
    :type period: int
    :param max_anomaly_ratio: Optional argument, advanced model parameter, max
     anomaly ratio in a time series.
    :type max_anomaly_ratio: float
    :param sensitivity: Optional argument, advanced model parameter, between
     0-99, the lower the value is, the larger the margin value will be which
     means less anomalies will be accepted.
    :type sensitivity: int
    """

    _validation = {
        'timestamp': {'required': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'period': {'key': 'period', 'type': 'int'},
        'max_anomaly_ratio': {'key': 'maxAnomalyRatio', 'type': 'float'},
        'sensitivity': {'key': 'sensitivity', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AnomalyDetectOnTimestampRequest, self).__init__(**kwargs)
        self.timestamp = kwargs.get('timestamp', None)
        self.period = kwargs.get('period', None)
        self.max_anomaly_ratio = kwargs.get('max_anomaly_ratio', None)
        self.sensitivity = kwargs.get('sensitivity', None)