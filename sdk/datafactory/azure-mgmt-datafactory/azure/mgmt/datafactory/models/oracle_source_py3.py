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

from .copy_source_py3 import CopySource


class OracleSource(CopySource):
    """A copy activity Oracle source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param disable_metrics_collection: Specifies whether to disable collecting
     data source metrics. Type: boolean (or Expression with resultType
     boolean).
    :type disable_metrics_collection: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param oracle_reader_query: Oracle reader query. Type: string (or
     Expression with resultType string).
    :type oracle_reader_query: object
    :param query_timeout: Query timeout. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type query_timeout: object
    :param partition_option: The partition mechanism that will be used for
     oracle read in parallel.
    :type partition_option: object
    :param partition_settings: The settings that will be leveraged for oracle
     source partitioning.
    :type partition_settings:
     ~azure.mgmt.datafactory.models.OraclePartitionSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'disable_metrics_collection': {'key': 'disableMetricsCollection', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'oracle_reader_query': {'key': 'oracleReaderQuery', 'type': 'object'},
        'query_timeout': {'key': 'queryTimeout', 'type': 'object'},
        'partition_option': {'key': 'partitionOption', 'type': 'object'},
        'partition_settings': {'key': 'partitionSettings', 'type': 'OraclePartitionSettings'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, disable_metrics_collection=None, oracle_reader_query=None, query_timeout=None, partition_option=None, partition_settings=None, **kwargs) -> None:
        super(OracleSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections, disable_metrics_collection=disable_metrics_collection, **kwargs)
        self.oracle_reader_query = oracle_reader_query
        self.query_timeout = query_timeout
        self.partition_option = partition_option
        self.partition_settings = partition_settings
        self.type = 'OracleSource'
