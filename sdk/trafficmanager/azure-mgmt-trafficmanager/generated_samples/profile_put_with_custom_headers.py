# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.trafficmanager import TrafficManagerManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-trafficmanager
# USAGE
    python profile_put_with_custom_headers.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = TrafficManagerManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.profiles.create_or_update(
        resource_group_name="azuresdkfornetautoresttrafficmanager2583",
        profile_name="azuresdkfornetautoresttrafficmanager6192",
        parameters={
            "location": "global",
            "properties": {
                "dnsConfig": {"relativeName": "azuresdkfornetautoresttrafficmanager6192", "ttl": 35},
                "endpoints": [
                    {
                        "name": "My external endpoint",
                        "properties": {
                            "customHeaders": [{"name": "header-2", "value": "value-2-overridden"}],
                            "endpointLocation": "North Europe",
                            "endpointStatus": "Enabled",
                            "target": "foobar.contoso.com",
                        },
                        "type": "Microsoft.network/TrafficManagerProfiles/ExternalEndpoints",
                    }
                ],
                "monitorConfig": {
                    "customHeaders": [
                        {"name": "header-1", "value": "value-1"},
                        {"name": "header-2", "value": "value-2"},
                    ],
                    "expectedStatusCodeRanges": [{"max": 205, "min": 200}, {"max": 410, "min": 400}],
                    "intervalInSeconds": 10,
                    "path": "/testpath.aspx",
                    "port": 80,
                    "protocol": "HTTP",
                    "timeoutInSeconds": 5,
                    "toleratedNumberOfFailures": 2,
                },
                "profileStatus": "Enabled",
                "trafficRoutingMethod": "Performance",
                "trafficViewEnrollmentStatus": "Disabled",
            },
        },
    )
    print(response)


# x-ms-original-file: specification/trafficmanager/resource-manager/Microsoft.Network/preview/2022-04-01-preview/examples/Profile-PUT-WithCustomHeaders.json
if __name__ == "__main__":
    main()
