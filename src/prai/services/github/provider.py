from prai.models.github import User
from prai.services.github.make_request import GithubRequestProvider


class GithubProvider:
    def __init__(self):
        self.request_provider = GithubRequestProvider()

    async def get_current_user(self) -> User:
        """Get the current authenticated GitHub user."""
        return User(**await self.request_provider.make_request("/user"))
