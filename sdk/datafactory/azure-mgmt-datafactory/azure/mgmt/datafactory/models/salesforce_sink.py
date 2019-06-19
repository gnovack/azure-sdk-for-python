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

from .copy_sink import CopySink


class SalesforceSink(CopySink):
    """A copy activity Salesforce sink.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param write_batch_size: Write batch size. Type: integer (or Expression
     with resultType integer), minimum: 0.
    :type write_batch_size: object
    :param write_batch_timeout: Write batch timeout. Type: string (or
     Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type write_batch_timeout: object
    :param sink_retry_count: Sink retry count. Type: integer (or Expression
     with resultType integer).
    :type sink_retry_count: object
    :param sink_retry_wait: Sink retry wait. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type sink_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the sink data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param disable_metrics_collection: Specifies whether to disable collecting
     data source metrics. Type: boolean (or Expression with resultType
     boolean).
    :type disable_metrics_collection: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param write_behavior: The write behavior for the operation. Default is
     Insert.
    :type write_behavior: object
    :param external_id_field_name: The name of the external ID field for
     upsert operation. Default value is 'Id' column. Type: string (or
     Expression with resultType string).
    :type external_id_field_name: object
    :param ignore_null_values: The flag indicating whether or not to ignore
     null values from input dataset (except key fields) during write operation.
     Default value is false. If set it to true, it means ADF will leave the
     data in the destination object unchanged when doing upsert/update
     operation and insert defined default value when doing insert operation,
     versus ADF will update the data in the destination object to NULL when
     doing upsert/update operation and insert NULL value when doing insert
     operation. Type: boolean (or Expression with resultType boolean).
    :type ignore_null_values: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'write_batch_size': {'key': 'writeBatchSize', 'type': 'object'},
        'write_batch_timeout': {'key': 'writeBatchTimeout', 'type': 'object'},
        'sink_retry_count': {'key': 'sinkRetryCount', 'type': 'object'},
        'sink_retry_wait': {'key': 'sinkRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'disable_metrics_collection': {'key': 'disableMetricsCollection', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'write_behavior': {'key': 'writeBehavior', 'type': 'object'},
        'external_id_field_name': {'key': 'externalIdFieldName', 'type': 'object'},
        'ignore_null_values': {'key': 'ignoreNullValues', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(SalesforceSink, self).__init__(**kwargs)
        self.write_behavior = kwargs.get('write_behavior', None)
        self.external_id_field_name = kwargs.get('external_id_field_name', None)
        self.ignore_null_values = kwargs.get('ignore_null_values', None)
        self.type = 'SalesforceSink'
