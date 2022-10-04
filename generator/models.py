from datetime import date
from typing import List, Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic_yaml import YamlModel


class BaseModel(PydanticBaseModel):
    condensed: bool = False


class DateRange(PydanticBaseModel):
    start_date: date
    end_date: date


class Degree(BaseModel):
    college: str
    city_st: str
    dates: DateRange
    major: str
    degree: str


class Course(BaseModel):
    name: str
    date: date


class JobHighlight(BaseModel):
    text: str


class Job(BaseModel):
    title: str
    dates: List[DateRange]
    summary: str
    highlights: List[JobHighlight]


class Employer(BaseModel):
    name: str
    city_st: str
    positions: List[Job]


class Tech(BaseModel):
    name: str


class TechCategory(PydanticBaseModel):
    entries: List[Tech]


class Resume(YamlModel):
    hardware: TechCategory
    operating_systems: TechCategory
    applications: TechCategory
    cloud: TechCategory
    programming: TechCategory
    experience: List[Employer]
    courses: List[Course]
    education: List[Degree]
