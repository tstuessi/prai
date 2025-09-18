import pytest
from unittest.mock import AsyncMock, MagicMock
from aiohttp import ClientResponseError

from prai.services.github.provider import GithubProvider
from prai.services.github.make_request import GithubRequestProvider
from prai.models.github import UserGet, PullRequestGet
from tests.factories import PrivateUserFactory, PullRequestGetFactory


class TestGithubProvider:
    """Tests for the GitHub provider functionality."""

    @pytest.fixture
    def provider_with_mock_request(self):
        """Create a GithubProvider with mocked request provider."""
        request_provider = AsyncMock(spec=GithubRequestProvider)
        provider = GithubProvider(request_provider=request_provider)
        return provider

    def test_init_creates_request_provider(self):
        """Test that initialization creates a GithubRequestProvider instance."""
        provider = GithubProvider()
        assert isinstance(provider.request_provider, GithubRequestProvider)

    @pytest.mark.asyncio
    async def test_get_current_user(self, provider_with_mock_request):
        """Test get_current_user calls correct endpoint and returns UserGet."""
        user_data = PrivateUserFactory.build().__dict__
        provider_with_mock_request.request_provider.make_request.return_value = user_data

        result = await provider_with_mock_request.get_current_user()

        assert isinstance(result, UserGet)
        provider_with_mock_request.request_provider.make_request.assert_called_once_with("/user")

    @pytest.mark.asyncio
    async def test_get_current_user_propagates_errors(self, provider_with_mock_request):
        """Test that errors from request provider are propagated."""
        error = ClientResponseError(request_info=MagicMock(), history=(), status=401)
        provider_with_mock_request.request_provider.make_request.side_effect = error

        with pytest.raises(ClientResponseError):
            await provider_with_mock_request.get_current_user()

    @pytest.mark.asyncio
    async def test_get_pull_request(self, provider_with_mock_request):
        """Test get_pull_request calls correct endpoint and returns PullRequestGet."""
        pr_data: PullRequestGet = PullRequestGetFactory.build()
        provider_with_mock_request.request_provider.make_request.return_value = pr_data.model_dump(
            mode="json", by_alias=True
        )

        result = await provider_with_mock_request.get_pull_request("owner", "repo", 123)

        assert isinstance(result, PullRequestGet)
        provider_with_mock_request.request_provider.make_request.assert_called_once_with("/repos/owner/repo/pulls/123")

    @pytest.mark.asyncio
    async def test_get_pull_request_propagates_errors(self, provider_with_mock_request):
        """Test that errors from request provider are propagated."""
        error = ClientResponseError(request_info=MagicMock(), history=(), status=404)
        provider_with_mock_request.request_provider.make_request.side_effect = error

        with pytest.raises(ClientResponseError):
            await provider_with_mock_request.get_pull_request("owner", "repo", 123)
