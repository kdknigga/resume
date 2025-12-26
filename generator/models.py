"""Models for resume data."""

from typing import TYPE_CHECKING

from pydantic import BaseModel as PydanticBaseModel
from pydantic_yaml import YamlModel

if TYPE_CHECKING:
    from datetime import date


class BaseModel(PydanticBaseModel):
    """Base model with common config."""

    condensed: bool = False


class DateRange(PydanticBaseModel):
    """A date range with a start and end date."""

    start_date: date
    end_date: date


class Degree(BaseModel):
    """A degree earned at a college or university."""

    college: str
    city_st: str
    dates: DateRange
    major: str
    degree: str


class Course(BaseModel):
    """A course taken outside of the pursuit of a degree."""

    name: str
    date: date


class JobHighlight(BaseModel):
    """A highlight or key achievement within a job."""

    text: str


class Job(BaseModel):
    """A job held within an employer."""

    title: str
    dates: list[DateRange]
    summary: str | None
    highlights: list[JobHighlight] | None


class Employer(BaseModel):
    """An employer with one or more positions held."""

    name: str
    city_st: str
    positions: list[Job]


class Tech(BaseModel):
    """A technology or tool used in the resume."""

    name: str


class TechCategory(PydanticBaseModel):
    """A category of technologies or tools."""

    entries: list[Tech]


class Resume(YamlModel):
    """A resume model."""

    hardware: TechCategory
    operating_systems: TechCategory
    applications: TechCategory
    cloud: TechCategory
    programming: TechCategory
    experience: list[Employer]
    courses: list[Course]
    education: list[Degree]
