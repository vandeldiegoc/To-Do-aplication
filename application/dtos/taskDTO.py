from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Status(Enum):
    active = "active"
    progress = "progress"
    pinish = "finish"
    incomplete = "Incomplete"


class TaskDTO(BaseModel):
    name: str
    description: str
    create_data: datetime
    status: Status
    deadline: bool
    finish_date: Optional[datetime]
    start_date: Optional[datetime]


class Task(BaseModel):
    task_id: str
    name: str
    description: str
    create_data: datetime
    status: Status
    deadline: bool
    finish_date: Optional[datetime]
    start_date: Optional[datetime]
