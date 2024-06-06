from typing import Protocol

from application.dtos.taskDTO import Task, TaskDTO


class managerNote(Protocol):
    def createNote(self, prop: TaskDTO) -> Task:
        ...
