# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class AzureMonitorWorkspace(_serialization.Model):
    """Properties of an Azure Monitor workspace.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar account_id: The immutable ID of the Azure Monitor workspace. This property is read-only.
    :vartype account_id: str
    :ivar metrics: Information about metrics for the Azure Monitor workspace.
    :vartype metrics:
     ~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceMetrics
    :ivar provisioning_state: The provisioning state of the Azure Monitor workspace. Set to
     Succeeded if everything is healthy. Known values are: "Creating", "Succeeded", "Deleting",
     "Failed", and "Canceled".
    :vartype provisioning_state: str or
     ~$(python-base-namespace).v2021_06_03_preview.models.ProvisioningState
    :ivar default_ingestion_settings: The Data Collection Rule and Endpoint used for ingestion by
     default.
    :vartype default_ingestion_settings:
     ~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceDefaultIngestionSettings
    """

    _validation = {
        "account_id": {"readonly": True},
        "metrics": {"readonly": True},
        "provisioning_state": {"readonly": True},
        "default_ingestion_settings": {"readonly": True},
    }

    _attribute_map = {
        "account_id": {"key": "accountId", "type": "str"},
        "metrics": {"key": "metrics", "type": "AzureMonitorWorkspaceMetrics"},
        "provisioning_state": {"key": "provisioningState", "type": "str"},
        "default_ingestion_settings": {
            "key": "defaultIngestionSettings",
            "type": "AzureMonitorWorkspaceDefaultIngestionSettings",
        },
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.account_id = None
        self.metrics = None
        self.provisioning_state = None
        self.default_ingestion_settings = None


class IngestionSettings(_serialization.Model):
    """Settings for data ingestion.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar data_collection_rule_resource_id: The Azure resource Id of the default data collection
     rule for this workspace.
    :vartype data_collection_rule_resource_id: str
    :ivar data_collection_endpoint_resource_id: The Azure resource Id of the default data
     collection endpoint for this workspace.
    :vartype data_collection_endpoint_resource_id: str
    """

    _validation = {
        "data_collection_rule_resource_id": {"readonly": True},
        "data_collection_endpoint_resource_id": {"readonly": True},
    }

    _attribute_map = {
        "data_collection_rule_resource_id": {"key": "dataCollectionRuleResourceId", "type": "str"},
        "data_collection_endpoint_resource_id": {"key": "dataCollectionEndpointResourceId", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.data_collection_rule_resource_id = None
        self.data_collection_endpoint_resource_id = None


class AzureMonitorWorkspaceDefaultIngestionSettings(IngestionSettings):
    """The Data Collection Rule and Endpoint used for ingestion by default.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar data_collection_rule_resource_id: The Azure resource Id of the default data collection
     rule for this workspace.
    :vartype data_collection_rule_resource_id: str
    :ivar data_collection_endpoint_resource_id: The Azure resource Id of the default data
     collection endpoint for this workspace.
    :vartype data_collection_endpoint_resource_id: str
    """

    _validation = {
        "data_collection_rule_resource_id": {"readonly": True},
        "data_collection_endpoint_resource_id": {"readonly": True},
    }

    _attribute_map = {
        "data_collection_rule_resource_id": {"key": "dataCollectionRuleResourceId", "type": "str"},
        "data_collection_endpoint_resource_id": {"key": "dataCollectionEndpointResourceId", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class Metrics(_serialization.Model):
    """Information about metrics for the workspace.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar prometheus_query_endpoint: The Prometheus query endpoint for the workspace.
    :vartype prometheus_query_endpoint: str
    :ivar internal_id: An internal identifier for the metrics container. Only to be used by the
     system.
    :vartype internal_id: str
    """

    _validation = {
        "prometheus_query_endpoint": {"readonly": True},
        "internal_id": {"readonly": True},
    }

    _attribute_map = {
        "prometheus_query_endpoint": {"key": "prometheusQueryEndpoint", "type": "str"},
        "internal_id": {"key": "internalId", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.prometheus_query_endpoint = None
        self.internal_id = None


class AzureMonitorWorkspaceMetrics(Metrics):
    """Information about metrics for the Azure Monitor workspace.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar prometheus_query_endpoint: The Prometheus query endpoint for the workspace.
    :vartype prometheus_query_endpoint: str
    :ivar internal_id: An internal identifier for the metrics container. Only to be used by the
     system.
    :vartype internal_id: str
    """

    _validation = {
        "prometheus_query_endpoint": {"readonly": True},
        "internal_id": {"readonly": True},
    }

    _attribute_map = {
        "prometheus_query_endpoint": {"key": "prometheusQueryEndpoint", "type": "str"},
        "internal_id": {"key": "internalId", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~$(python-base-namespace).v2021_06_03_preview.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~$(python-base-namespace).v2021_06_03_preview.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class AzureMonitorWorkspaceResource(TrackedResource):  # pylint: disable=too-many-instance-attributes
    """An Azure Monitor Workspace definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~$(python-base-namespace).v2021_06_03_preview.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar etag: Resource entity tag (ETag).
    :vartype etag: str
    :ivar account_id: The immutable ID of the Azure Monitor workspace. This property is read-only.
    :vartype account_id: str
    :ivar metrics: Information about metrics for the Azure Monitor workspace.
    :vartype metrics:
     ~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceMetrics
    :ivar provisioning_state: The provisioning state of the Azure Monitor workspace. Set to
     Succeeded if everything is healthy. Known values are: "Creating", "Succeeded", "Deleting",
     "Failed", and "Canceled".
    :vartype provisioning_state: str or
     ~$(python-base-namespace).v2021_06_03_preview.models.ProvisioningState
    :ivar default_ingestion_settings: The Data Collection Rule and Endpoint used for ingestion by
     default.
    :vartype default_ingestion_settings:
     ~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceDefaultIngestionSettings
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "etag": {"readonly": True},
        "account_id": {"readonly": True},
        "metrics": {"readonly": True},
        "provisioning_state": {"readonly": True},
        "default_ingestion_settings": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "etag": {"key": "etag", "type": "str"},
        "account_id": {"key": "properties.accountId", "type": "str"},
        "metrics": {"key": "properties.metrics", "type": "AzureMonitorWorkspaceMetrics"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "default_ingestion_settings": {
            "key": "properties.defaultIngestionSettings",
            "type": "AzureMonitorWorkspaceDefaultIngestionSettings",
        },
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.etag = None
        self.account_id = None
        self.metrics = None
        self.provisioning_state = None
        self.default_ingestion_settings = None


class AzureMonitorWorkspaceResourceForUpdate(_serialization.Model):
    """Definition of ARM tracked top level resource properties for update operation.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.tags = tags


class AzureMonitorWorkspaceResourceListResult(_serialization.Model):
    """A pageable list of resources.

    All required parameters must be populated in order to send to Azure.

    :ivar value: A list of resources. Required.
    :vartype value:
     list[~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceResource]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[AzureMonitorWorkspaceResource]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: List["_models.AzureMonitorWorkspaceResource"], next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: A list of resources. Required.
        :paramtype value:
         list[~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceResource]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class AzureMonitorWorkspaceResourceProperties(AzureMonitorWorkspace):
    """Resource properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar account_id: The immutable ID of the Azure Monitor workspace. This property is read-only.
    :vartype account_id: str
    :ivar metrics: Information about metrics for the Azure Monitor workspace.
    :vartype metrics:
     ~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceMetrics
    :ivar provisioning_state: The provisioning state of the Azure Monitor workspace. Set to
     Succeeded if everything is healthy. Known values are: "Creating", "Succeeded", "Deleting",
     "Failed", and "Canceled".
    :vartype provisioning_state: str or
     ~$(python-base-namespace).v2021_06_03_preview.models.ProvisioningState
    :ivar default_ingestion_settings: The Data Collection Rule and Endpoint used for ingestion by
     default.
    :vartype default_ingestion_settings:
     ~$(python-base-namespace).v2021_06_03_preview.models.AzureMonitorWorkspaceDefaultIngestionSettings
    """

    _validation = {
        "account_id": {"readonly": True},
        "metrics": {"readonly": True},
        "provisioning_state": {"readonly": True},
        "default_ingestion_settings": {"readonly": True},
    }

    _attribute_map = {
        "account_id": {"key": "accountId", "type": "str"},
        "metrics": {"key": "metrics", "type": "AzureMonitorWorkspaceMetrics"},
        "provisioning_state": {"key": "provisioningState", "type": "str"},
        "default_ingestion_settings": {
            "key": "defaultIngestionSettings",
            "type": "AzureMonitorWorkspaceDefaultIngestionSettings",
        },
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~$(python-base-namespace).v2021_06_03_preview.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~$(python-base-namespace).v2021_06_03_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~$(python-base-namespace).v2021_06_03_preview.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error object.
        :paramtype error: ~$(python-base-namespace).v2021_06_03_preview.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class Operation(_serialization.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for ARM/control-plane operations.
    :vartype is_data_action: bool
    :ivar display: Localized display information for this particular operation.
    :vartype display: ~$(python-base-namespace).v2021_06_03_preview.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Known values are: "user", "system",
     and "user,system".
    :vartype origin: str or ~$(python-base-namespace).v2021_06_03_preview.models.Origin
    :ivar action_type: Enum. Indicates the action type. "Internal" refers to actions that are for
     internal only APIs. "Internal"
    :vartype action_type: str or ~$(python-base-namespace).v2021_06_03_preview.models.ActionType
    """

    _validation = {
        "name": {"readonly": True},
        "is_data_action": {"readonly": True},
        "origin": {"readonly": True},
        "action_type": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "is_data_action": {"key": "isDataAction", "type": "bool"},
        "display": {"key": "display", "type": "OperationDisplay"},
        "origin": {"key": "origin", "type": "str"},
        "action_type": {"key": "actionType", "type": "str"},
    }

    def __init__(self, *, display: Optional["_models.OperationDisplay"] = None, **kwargs: Any) -> None:
        """
        :keyword display: Localized display information for this particular operation.
        :paramtype display: ~$(python-base-namespace).v2021_06_03_preview.models.OperationDisplay
        """
        super().__init__(**kwargs)
        self.name = None
        self.is_data_action = None
        self.display = display
        self.origin = None
        self.action_type = None


class OperationDisplay(_serialization.Model):
    """Localized display information for this particular operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    _validation = {
        "provider": {"readonly": True},
        "resource": {"readonly": True},
        "operation": {"readonly": True},
        "description": {"readonly": True},
    }

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(_serialization.Model):
    """A list of REST API operations supported by an Azure Resource Provider. It contains an URL link
    to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of operations supported by the resource provider.
    :vartype value: list[~$(python-base-namespace).v2021_06_03_preview.models.Operation]
    :ivar next_link: URL to get the next set of operation list results (if there are any).
    :vartype next_link: str
    """

    _validation = {
        "value": {"readonly": True},
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.value = None
        self.next_link = None


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or
     ~$(python-base-namespace).v2021_06_03_preview.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or
     ~$(python-base-namespace).v2021_06_03_preview.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or
         ~$(python-base-namespace).v2021_06_03_preview.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or
         ~$(python-base-namespace).v2021_06_03_preview.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
