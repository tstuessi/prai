from fastapi import APIRouter

from prai.models.github import User
from prai.services.github.provider import GithubProvider

router = APIRouter(prefix="/api/github", tags=["github"])

github_provider = GithubProvider()


@router.get("/user")
async def get_github_user() -> User:
    return await github_provider.get_current_user()
