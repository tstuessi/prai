import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from aiohttp import ClientResponseError

from prai.services.github.provider import GithubProvider
from prai.services.github.make_request import GithubRequestProvider
from prai.models.github import User, PrivateUser, PublicUser
from tests.factories import PrivateUserFactory, PublicUserFactory


class TestGithubProvider:
    """Tests for the GitHub provider functionality."""

    @pytest.fixture
    def provider(self):
        """Create a GithubProvider instance for testing."""
        return GithubProvider()

    @pytest.fixture
    def mock_request_provider(self):
        """Create a mock GithubRequestProvider for testing."""
        return AsyncMock(spec=GithubRequestProvider)

    @pytest.fixture
    def provider_with_mock_request(self, mock_request_provider):
        """Create a GithubProvider with mocked request provider."""
        provider = GithubProvider()
        provider.request_provider = mock_request_provider
        return provider

    def test_init_creates_request_provider(self):
        """Test that initialization creates a GithubRequestProvider instance."""
        provider = GithubProvider()

        assert isinstance(provider.request_provider, GithubRequestProvider)

    @pytest.mark.asyncio
    async def test_get_current_user_success_private_user(self, provider_with_mock_request):
        """Test successful retrieval of current user (private user data)."""
        # Create mock private user data
        private_user_data = PrivateUserFactory.build().__dict__
        provider_with_mock_request.request_provider.make_request.return_value = private_user_data

        result = await provider_with_mock_request.get_current_user()

        assert isinstance(result, User)
        assert isinstance(result.root, PrivateUser)
        assert result.root.login == private_user_data["login"]
        assert result.root.id == private_user_data["id"]
        provider_with_mock_request.request_provider.make_request.assert_called_once_with("/user")

    @pytest.mark.asyncio
    async def test_get_current_user_success_public_user(self, provider_with_mock_request):
        """Test successful retrieval of current user (public user data)."""
        # Create mock public user data without private fields
        public_user_data = PublicUserFactory.build().__dict__
        # Remove private fields that would make it a PrivateUser
        public_user_data.pop("private_gists", None)
        public_user_data.pop("total_private_repos", None)
        public_user_data.pop("owned_private_repos", None)
        public_user_data.pop("two_factor_authentication", None)
        public_user_data.pop("business_plus", None)
        public_user_data.pop("ldap_dn", None)

        provider_with_mock_request.request_provider.make_request.return_value = public_user_data

        result = await provider_with_mock_request.get_current_user()

        assert isinstance(result, User)
        assert isinstance(result.root, PublicUser)
        assert result.root.login == public_user_data["login"]
        assert result.root.id == public_user_data["id"]
        provider_with_mock_request.request_provider.make_request.assert_called_once_with("/user")

    @pytest.mark.asyncio
    async def test_get_current_user_calls_correct_endpoint(self, provider_with_mock_request):
        """Test that get_current_user calls the correct GitHub API endpoint."""
        mock_user_data = PrivateUserFactory.build().__dict__
        provider_with_mock_request.request_provider.make_request.return_value = mock_user_data

        await provider_with_mock_request.get_current_user()

        provider_with_mock_request.request_provider.make_request.assert_called_once_with("/user")

    @pytest.mark.asyncio
    async def test_get_current_user_propagates_http_errors(self, provider_with_mock_request):
        """Test that HTTP errors from the request provider are propagated."""
        error = ClientResponseError(request_info=MagicMock(), history=(), status=401)
        provider_with_mock_request.request_provider.make_request.side_effect = error

        with pytest.raises(ClientResponseError):
            await provider_with_mock_request.get_current_user()

        provider_with_mock_request.request_provider.make_request.assert_called_once_with("/user")

    @pytest.mark.asyncio
    async def test_get_current_user_with_minimal_data(self, provider_with_mock_request):
        """Test user creation with minimal required fields."""
        minimal_user_data = {
            "login": "testuser",
            "id": 123,
            "node_id": "MDQ6VXNlcjEyMw==",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": None,
            "url": "https://api.github.com/users/testuser",
            "html_url": "https://github.com/testuser",
            "followers_url": "https://api.github.com/users/testuser/followers",
            "following_url": "https://api.github.com/users/testuser/following{/other_user}",
            "gists_url": "https://api.github.com/users/testuser/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/testuser/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/testuser/subscriptions",
            "organizations_url": "https://api.github.com/users/testuser/orgs",
            "repos_url": "https://api.github.com/users/testuser/repos",
            "events_url": "https://api.github.com/users/testuser/events{/privacy}",
            "received_events_url": "https://api.github.com/users/testuser/received_events",
            "type": "User",
            "site_admin": False,
            "name": None,
            "company": None,
            "blog": None,
            "location": None,
            "email": None,
            "hireable": None,
            "bio": None,
            "public_repos": 0,
            "public_gists": 0,
            "followers": 0,
            "following": 0,
            "created_at": "2023-01-01T00:00:00Z",
            "updated_at": "2023-01-01T00:00:00Z",
        }
        provider_with_mock_request.request_provider.make_request.return_value = minimal_user_data

        result = await provider_with_mock_request.get_current_user()

        assert isinstance(result, User)
        assert result.root.login == "testuser"
        assert result.root.id == 123

    @pytest.mark.asyncio
    async def test_get_current_user_handles_validation_errors(self, provider_with_mock_request):
        """Test that validation errors are raised for invalid user data."""
        invalid_user_data = {
            "login": "testuser",
            # Missing required fields like id, node_id, etc.
        }
        provider_with_mock_request.request_provider.make_request.return_value = invalid_user_data

        with pytest.raises(Exception):  # Pydantic validation error
            await provider_with_mock_request.get_current_user()

    @pytest.mark.asyncio
    async def test_get_current_user_with_plan_data(self, provider_with_mock_request):
        """Test user creation with plan information."""
        user_data = PrivateUserFactory.build().__dict__
        user_data["plan"] = {"collaborators": 25, "name": "pro", "space": 976562499, "private_repos": 9999}
        provider_with_mock_request.request_provider.make_request.return_value = user_data

        result = await provider_with_mock_request.get_current_user()

        assert isinstance(result, User)
        assert isinstance(result.root, PrivateUser)
        assert result.root.plan is not None
        assert result.root.plan.name == "pro"
        assert result.root.plan.collaborators == 25

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

    @pytest.mark.asyncio
    async def test_get_current_user_request_provider_integration(self, mock_aiohttp_session):
        """Test integration with actual GithubRequestProvider (mocked at aiohttp level)."""
        mock_session, mock_response = mock_aiohttp_session
        mock_user_data = PrivateUserFactory.build().__dict__
        mock_response.json.return_value = mock_user_data
        mock_response.raise_for_status.return_value = None

        # Test with real provider but mocked HTTP
        provider = GithubProvider()
        result = await provider.get_current_user()

        assert isinstance(result, User)
        assert result.root.login == mock_user_data["login"]
        mock_session.request.assert_called_once()
        call_args = mock_session.request.call_args
        assert "/user" in call_args[0][1]  # URL contains /user endpoint
