import logging
from typing import Optional
from prai.models.github import UserGet, PullRequestGet
from prai.services.github.make_request import GithubRequestProvider


class GithubProvider:
    def __init__(self, request_provider: Optional[GithubRequestProvider] = None):
        self.request_provider = request_provider or GithubRequestProvider()
        self.logger = logging.getLogger(__name__)

    async def get_current_user(self) -> UserGet:
        """Get the current authenticated GitHub user."""
        resp = await self.request_provider.make_request("/user")
        return UserGet.model_validate(resp)

    async def get_pull_request(self, owner: str, repo: str, pr_number: int) -> PullRequestGet:
        """Get a specific pull request by owner, repo, and PR number."""
        endpoint = f"/repos/{owner}/{repo}/pulls/{pr_number}"
        resp = await self.request_provider.make_request(endpoint)
        return PullRequestGet.model_validate(resp)
