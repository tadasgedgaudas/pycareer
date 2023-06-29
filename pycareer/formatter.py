from rich.console import Console
from rich.table import Table

from pycareer.models import Job


def format_job_table(jobs: list[Job]):
    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Company")
    table.add_column("Location")
    table.add_column("Salary")
    table.add_column("URL")
    table.add_column("Date")

    for job in jobs:
        table.add_row(job.id, job.title, job.company or "-", job.location or "-", job.salary or "-", job.url, job.date)
        table.add_row()

    console.print(table)
