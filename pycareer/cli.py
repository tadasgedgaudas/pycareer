import asyncio
from typing import Optional

import structlog
import typer

from pycareer.formatter import format_job_table
from pycareer.request import JobRequester

app = typer.Typer()
log = structlog.get_logger()


def build_kwargs(tag: str | None, location: str | None, limit: int) -> dict[str, str | int]:
    kwargs: dict[str, str | int] = {}
    if tag:
        kwargs["tag"] = tag
    if location:
        kwargs["location"] = location
    kwargs["limit"] = limit
    return kwargs


async def get_jobs(tag: str | None, location: str | None, limit: int) -> None:
    job_requester = JobRequester()
    kwargs = build_kwargs(tag, location, limit)
    jobs_response = await job_requester.request_jobs(**kwargs)
    await job_requester.session.close()
    format_job_table(jobs_response)


@app.command()
def jobs(
    limit: int = typer.Option(5, help="Limit the number of jobs to display"),
    tag: Optional[str] = None,
    location: Optional[str] = None,
):
    log.info("Getting jobs...")
    asyncio.run(get_jobs(tag, location, limit))


def main():
    app()
