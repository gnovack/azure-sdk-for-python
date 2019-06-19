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

from .copy_sink_py3 import CopySink


class AzureTableSink(CopySink):
    """A copy activity Azure Table sink.

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
    :param azure_table_default_partition_key_value: Azure Table default
     partition key value. Type: string (or Expression with resultType string).
    :type azure_table_default_partition_key_value: object
    :param azure_table_partition_key_name: Azure Table partition key name.
     Type: string (or Expression with resultType string).
    :type azure_table_partition_key_name: object
    :param azure_table_row_key_name: Azure Table row key name. Type: string
     (or Expression with resultType string).
    :type azure_table_row_key_name: object
    :param azure_table_insert_type: Azure Table insert type. Type: string (or
     Expression with resultType string).
    :type azure_table_insert_type: object
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
        'azure_table_default_partition_key_value': {'key': 'azureTableDefaultPartitionKeyValue', 'type': 'object'},
        'azure_table_partition_key_name': {'key': 'azureTablePartitionKeyName', 'type': 'object'},
        'azure_table_row_key_name': {'key': 'azureTableRowKeyName', 'type': 'object'},
        'azure_table_insert_type': {'key': 'azureTableInsertType', 'type': 'object'},
    }

    def __init__(self, *, additional_properties=None, write_batch_size=None, write_batch_timeout=None, sink_retry_count=None, sink_retry_wait=None, max_concurrent_connections=None, disable_metrics_collection=None, azure_table_default_partition_key_value=None, azure_table_partition_key_name=None, azure_table_row_key_name=None, azure_table_insert_type=None, **kwargs) -> None:
        super(AzureTableSink, self).__init__(additional_properties=additional_properties, write_batch_size=write_batch_size, write_batch_timeout=write_batch_timeout, sink_retry_count=sink_retry_count, sink_retry_wait=sink_retry_wait, max_concurrent_connections=max_concurrent_connections, disable_metrics_collection=disable_metrics_collection, **kwargs)
        self.azure_table_default_partition_key_value = azure_table_default_partition_key_value
        self.azure_table_partition_key_name = azure_table_partition_key_name
        self.azure_table_row_key_name = azure_table_row_key_name
        self.azure_table_insert_type = azure_table_insert_type
        self.type = 'AzureTableSink'
