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


class HttpSource(CopySource):
    """A copy activity source for an HTTP file.

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
    :param http_request_timeout: Specifies the timeout for a HTTP client to
     get HTTP response from HTTP server. The default value is equivalent to
     System.Net.HttpWebRequest.Timeout. Type: string (or Expression with
     resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type http_request_timeout: object
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
        'http_request_timeout': {'key': 'httpRequestTimeout', 'type': 'object'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, disable_metrics_collection=None, http_request_timeout=None, **kwargs) -> None:
        super(HttpSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections, disable_metrics_collection=disable_metrics_collection, **kwargs)
        self.http_request_timeout = http_request_timeout
        self.type = 'HttpSource'
