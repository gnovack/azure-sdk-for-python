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

from .tags_resource import TagsResource


class UpdateIotSecuritySolutionData(TagsResource):
    """UpdateIotSecuritySolutionData.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param user_defined_resources:
    :type user_defined_resources:
     ~azure.mgmt.security.models.UserDefinedResourcesProperties
    :param recommendations_configuration:
    :type recommendations_configuration:
     list[~azure.mgmt.security.models.RecommendationConfigurationProperties]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'user_defined_resources': {'key': 'userDefinedResources', 'type': 'UserDefinedResourcesProperties'},
        'recommendations_configuration': {'key': 'recommendationsConfiguration', 'type': '[RecommendationConfigurationProperties]'},
    }

    def __init__(self, **kwargs):
        super(UpdateIotSecuritySolutionData, self).__init__(**kwargs)
        self.user_defined_resources = kwargs.get('user_defined_resources', None)
        self.recommendations_configuration = kwargs.get('recommendations_configuration', None)
