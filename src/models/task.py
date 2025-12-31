"""Task data model for the Todo CLI application."""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a todo task.

    Attributes:
        id: Unique identifier (auto-assigned by TaskManager)
        title: Brief description of the task (required)
        description: Optional detailed description
        completed: Whether the task is complete (default: False)
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False
