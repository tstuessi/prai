import logging
import os
from typing import Optional
from prai.services.github.config import GitHubSettings
import aiohttp


logger = logging.getLogger(__name__)


class GithubRequestProvider:
    def __init__(self, config: Optional[GitHubSettings] = None):
        if config is None:
            config = GitHubSettings()
        self.token = config.TOKEN
        self.base_url = "https://api.github.com"
        self.headers = {
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
        }

    async def make_request(
        self, endpoint: str, method: str = "GET", headers: Optional[dict[str, str]] = None, data: Optional[dict] = None
    ):
        if endpoint.startswith("/"):
            endpoint = endpoint[1:]
        url = os.path.join(self.base_url, endpoint)
        headers = {**self.headers, **(headers or {})}
        async with aiohttp.ClientSession() as session:
            logger.debug(f"Making {method} request to {url}")
            async with session.request(method, url, headers=headers, json=data) as response:
                response.raise_for_status()
                return await response.json()
