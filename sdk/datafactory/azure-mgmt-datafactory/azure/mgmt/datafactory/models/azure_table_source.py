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

from .copy_source import CopySource


class AzureTableSource(CopySource):
    """A copy activity Azure Table source.

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
    :param azure_table_source_query: Azure Table source query. Type: string
     (or Expression with resultType string).
    :type azure_table_source_query: object
    :param azure_table_source_ignore_table_not_found: Azure Table source
     ignore table not found. Type: boolean (or Expression with resultType
     boolean).
    :type azure_table_source_ignore_table_not_found: object
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
        'azure_table_source_query': {'key': 'azureTableSourceQuery', 'type': 'object'},
        'azure_table_source_ignore_table_not_found': {'key': 'azureTableSourceIgnoreTableNotFound', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(AzureTableSource, self).__init__(**kwargs)
        self.azure_table_source_query = kwargs.get('azure_table_source_query', None)
        self.azure_table_source_ignore_table_not_found = kwargs.get('azure_table_source_ignore_table_not_found', None)
        self.type = 'AzureTableSource'
