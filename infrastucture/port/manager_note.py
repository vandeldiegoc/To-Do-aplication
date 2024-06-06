
from typing import Protocol


class TaskDTO(BaseModel):


class managerNote(Protocol):

    def createNote(prop: TaskDTO) -> User:
        ...
