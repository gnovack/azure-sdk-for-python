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


class ServerCertificateCommonNames(Model):
    """Describes a list of server certificates referenced by common name that are
    used to secure the cluster.

    :param common_names: The list of server certificates referenced by common
     name that are used to secure the cluster.
    :type common_names:
     list[~azure.mgmt.servicefabric.models.ServerCertificateCommonName]
    :param x509_store_name: The local certificate store location. Possible
     values include: 'AddressBook', 'AuthRoot', 'CertificateAuthority',
     'Disallowed', 'My', 'Root', 'TrustedPeople', 'TrustedPublisher'
    :type x509_store_name: str or ~azure.mgmt.servicefabric.models.enum
    """

    _attribute_map = {
        'common_names': {'key': 'commonNames', 'type': '[ServerCertificateCommonName]'},
        'x509_store_name': {'key': 'x509StoreName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServerCertificateCommonNames, self).__init__(**kwargs)
        self.common_names = kwargs.get('common_names', None)
        self.x509_store_name = kwargs.get('x509_store_name', None)
