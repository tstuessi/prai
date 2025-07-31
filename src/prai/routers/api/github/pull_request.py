from fastapi import APIRouter

from prai.models.github import PullRequestGet
from prai.services.github.provider import GithubProvider

router = APIRouter(prefix="/api/github", tags=["github"])

github_provider = GithubProvider()


@router.get("/pull-request")
async def get_pull_request(owner: str, repo: str, pr_number: int) -> PullRequestGet:
    return await github_provider.get_pull_request(owner, repo, pr_number)
