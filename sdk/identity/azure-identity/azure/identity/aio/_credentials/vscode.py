# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import cast, Optional, Any, Tuple

from azure.core.credentials import AccessToken
from ..._exceptions import CredentialUnavailableError
from .._internal import AsyncContextManager
from .._internal.aad_client import AadClient
from .._internal.get_token_mixin import GetTokenMixin
from .._internal.decorators import log_get_token_async
from ..._credentials.vscode import _VSCodeCredentialBase


class VisualStudioCodeCredential(_VSCodeCredentialBase, AsyncContextManager, GetTokenMixin):
    """Authenticates as the Azure user signed in to Visual Studio Code via the 'Azure Account' extension.

    It's a `known issue <https://github.com/Azure/azure-sdk-for-python/issues/23249>`_ that this credential doesn't
    work with `Azure Account extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account>`_
    versions newer than **0.9.11**. A long-term fix to this problem is in progress. In the meantime, consider
    authenticating with :class:`AzureCliCredential`.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com".
        This argument is required for a custom cloud and usually unnecessary otherwise. Defaults to the authority
        matching the "Azure: Cloud" setting in VS Code's user settings or, when that setting has no value, the
        authority for Azure Public Cloud.
    :keyword str tenant_id: ID of the tenant the credential should authenticate in. Defaults to the "Azure: Tenant"
        setting in VS Code's user settings or, when that setting has no value, the "organizations" tenant, which
        supports only Azure Active Directory work or school accounts.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    """

    async def __aenter__(self) -> "VisualStudioCodeCredential":
        if self._client:
            await self._client.__aenter__()
        return self

    async def close(self) -> None:
        """Close the credential's transport session."""

        if self._client:
            await self._client.__aexit__()

    @log_get_token_async
    async def get_token(self, *scopes: str, **kwargs: Any) -> AccessToken:
        """Request an access token for `scopes` as the user currently signed in to Visual Studio Code.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str tenant_id: optional tenant to include in the token request.
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.identity.CredentialUnavailableError: the credential cannot retrieve user details from Visual
            Studio Code
        """
        if self._unavailable_reason:
            error_message = self._unavailable_reason \
                            + '\n' \
                              "Visit https://aka.ms/azsdk/python/identity/vscodecredential/troubleshoot" \
                              " to troubleshoot this issue."
            raise CredentialUnavailableError(message=error_message)
        if not self._client:
            raise CredentialUnavailableError("Initialization failed")

        return await super().get_token(*scopes, **kwargs)

    async def _acquire_token_silently(
        self, *scopes: str, **kwargs: Any
    ) -> Tuple[Optional[AccessToken], Optional[int]]:
        self._client = cast(AadClient, self._client)
        return self._client.get_cached_access_token(scopes, **kwargs), None

    async def _request_token(self, *scopes: str, **kwargs: Any) -> AccessToken:
        refresh_token = self._get_refresh_token()
        self._client = cast(AadClient, self._client)
        return await self._client.obtain_token_by_refresh_token(scopes, refresh_token, **kwargs)

    def _get_client(self, **kwargs: Any) -> AadClient:
        return AadClient(**kwargs)
