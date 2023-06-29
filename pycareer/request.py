from json import JSONDecodeError
from typing import Any

import aiohttp

from pycareer.models import Job


class JobRequester:
    def __init__(self):
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.api_url: str = "https://main.0xw.app/pycareer/jobs/get"

    @staticmethod
    def parse_job(job: dict[str, Any]) -> Job:
        return Job(
            id=job["id"],
            company=job["company_name"],
            title=job["job_title"],
            location=job["location"],
            salary=job["salary"],
            url=f"https://pycareer.io/jobs/{job['id']}",
            date=job["date"],
        )

    async def request_jobs(self, **kwargs: dict[str, Any]) -> list[Job]:
        response = await self.session.get(self.api_url, params=kwargs)
        try:
            data = await response.json()
        except JSONDecodeError:
            return []
        return [self.parse_job(job) for job in data["data"]]
