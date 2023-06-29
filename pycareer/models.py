from pydantic import BaseModel


class Job(BaseModel):
    id: str
    title: str
    company: str | None
    location: str | None
    salary: str | None
    url: str
    date: str
