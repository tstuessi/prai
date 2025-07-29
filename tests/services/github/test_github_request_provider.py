import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from aiohttp import ClientResponseError

from prai.services.github.make_request import GithubRequestProvider
from prai.services.github.config import GitHubSettings


class TestGithubRequestProvider:
    """Tests for the GitHub request provider functionality."""

    @pytest.fixture
    def mock_config(self):
        """Create a mock GitHub configuration for testing."""
        config = MagicMock(spec=GitHubSettings)
        config.TOKEN = "test_token_123"
        return config

    @pytest.fixture
    def provider(self, mock_config):
        """Create a GithubRequestProvider instance with mock config."""
        return GithubRequestProvider(config=mock_config)

    @pytest.fixture
    def provider_no_config(self):
        """Create a GithubRequestProvider instance without explicit config."""
        with patch("prai.services.github.make_request.GitHubSettings") as mock_settings:
            mock_settings.return_value.TOKEN = "default_token"
            return GithubRequestProvider()

    @pytest.fixture
    def mock_aiohttp_session(self):
        """Create a mock aiohttp ClientSession for testing."""
        with patch("aiohttp.ClientSession") as mock_session_class:
            mock_client_session = AsyncMock()
            mock_session = MagicMock()
            mock_response = AsyncMock()

            mock_client_session.__aenter__.return_value = mock_session
            mock_client_session.__aexit__.return_value = None
            mock_session.request.return_value.__aenter__.return_value = mock_response
            mock_session.request.return_value.__aexit__.return_value = None
            mock_response.json = AsyncMock()
            mock_response.raise_for_status = MagicMock()
            mock_session_class.return_value = mock_client_session

            yield mock_session, mock_response

    def test_init_with_config(self, mock_config):
        """Test provider initialization with explicit config."""
        provider = GithubRequestProvider(config=mock_config)

        assert provider.token == "test_token_123"
        assert provider.base_url == "https://api.github.com"
        assert provider.headers == {
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": "Bearer test_token_123",
            "Accept": "application/vnd.github+json",
        }

    def test_init_without_config(self):
        """Test provider initialization with default config."""
        with patch("prai.services.github.make_request.GitHubSettings") as mock_settings:
            mock_settings.return_value.TOKEN = "default_token"
            provider = GithubRequestProvider()

            assert provider.token == "default_token"
            assert provider.base_url == "https://api.github.com"
            mock_settings.assert_called_once()

    @pytest.mark.asyncio
    async def test_make_request_success(self, provider, mock_aiohttp_session):
        """Test successful API request with default parameters."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response_data = {"login": "testuser", "id": 12345}
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None

        result = await provider.make_request("user")

        assert result == mock_response_data
        mock_session.request.assert_called_once_with(
            "GET",
            "https://api.github.com/user",
            headers={
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": "Bearer test_token_123",
                "Accept": "application/vnd.github+json",
            },
            json=None,
        )

    @pytest.mark.asyncio
    async def test_make_request_with_leading_slash(self, provider, mock_aiohttp_session):
        """Test that leading slashes are properly stripped from endpoints."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response_data = {"data": "test"}
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None

        await provider.make_request("/repos/owner/repo")

        mock_session.request.assert_called_once_with(
            "GET",
            "https://api.github.com/repos/owner/repo",
            headers={
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": "Bearer test_token_123",
                "Accept": "application/vnd.github+json",
            },
            json=None,
        )

    @pytest.mark.asyncio
    async def test_make_request_with_custom_method(self, provider, mock_aiohttp_session):
        """Test API request with custom HTTP method."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response_data = {"created": True}
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None

        result = await provider.make_request("repos", method="POST")

        assert result == mock_response_data
        mock_session.request.assert_called_once_with(
            "POST",
            "https://api.github.com/repos",
            headers={
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": "Bearer test_token_123",
                "Accept": "application/vnd.github+json",
            },
            json=None,
        )

    @pytest.mark.asyncio
    async def test_make_request_with_custom_headers(self, provider, mock_aiohttp_session):
        """Test API request with additional custom headers."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response_data = {"data": "test"}
        custom_headers = {"Custom-Header": "custom-value"}
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None

        result = await provider.make_request("user", headers=custom_headers)

        assert result == mock_response_data
        expected_headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": "Bearer test_token_123",
            "Accept": "application/vnd.github+json",
            "Custom-Header": "custom-value",
        }
        mock_session.request.assert_called_once_with(
            "GET", "https://api.github.com/user", headers=expected_headers, json=None
        )

    @pytest.mark.asyncio
    async def test_make_request_with_data(self, provider, mock_aiohttp_session):
        """Test API request with JSON data payload."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response_data = {"created": True}
        request_data = {"name": "test-repo", "private": True}
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None

        result = await provider.make_request("user/repos", method="POST", data=request_data)

        assert result == mock_response_data
        mock_session.request.assert_called_once_with(
            "POST",
            "https://api.github.com/user/repos",
            headers={
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": "Bearer test_token_123",
                "Accept": "application/vnd.github+json",
            },
            json=request_data,
        )

    @pytest.mark.asyncio
    async def test_make_request_http_error(self, provider, mock_aiohttp_session):
        """Test API request handling of HTTP errors."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response.raise_for_status.side_effect = ClientResponseError(
            request_info=MagicMock(), history=(), status=404
        )

        with pytest.raises(ClientResponseError):
            await provider.make_request("nonexistent/endpoint")

        mock_response.raise_for_status.assert_called_once()

    @pytest.mark.asyncio
    async def test_make_request_logs_debug_info(self, provider, mock_aiohttp_session, caplog):
        """Test that debug logging works correctly for requests."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response_data = {"data": "test"}
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status.return_value = None

        with caplog.at_level("DEBUG"):
            await provider.make_request("user", method="POST")

        assert "Making POST request to https://api.github.com/user" in caplog.text

    @pytest.mark.parametrize(
        "endpoint,expected_url",
        [
            ("user", "https://api.github.com/user"),
            ("/user", "https://api.github.com/user"),
            ("repos/owner/repo", "https://api.github.com/repos/owner/repo"),
            ("/repos/owner/repo", "https://api.github.com/repos/owner/repo"),
            ("user/repos?sort=created", "https://api.github.com/user/repos?sort=created"),
        ],
    )
    @pytest.mark.asyncio
    async def test_endpoint_url_construction(self, provider, mock_aiohttp_session, endpoint, expected_url):
        """Test various endpoint formats produce correct URLs."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response.json.return_value = {}
        mock_response.raise_for_status.return_value = None

        await provider.make_request(endpoint)

        call_args = mock_session.request.call_args
        assert call_args[0][1] == expected_url

    @pytest.mark.parametrize("method", ["GET", "POST", "PUT", "PATCH", "DELETE"])
    @pytest.mark.asyncio
    async def test_different_http_methods(self, provider, mock_aiohttp_session, method):
        """Test that all common HTTP methods work correctly."""
        mock_session, mock_response = mock_aiohttp_session
        mock_response.json.return_value = {}
        mock_response.raise_for_status.return_value = None

        await provider.make_request("test", method=method)

        call_args = mock_session.request.call_args
        assert call_args[0][0] == method
