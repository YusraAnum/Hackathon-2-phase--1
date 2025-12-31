"""Task data model for the Todo CLI application."""

from dataclasses import dataclass
from enum import Enum


class Priority(Enum):
    """Task priority levels for sorting and visual display."""

    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

    @property
    def sort_order(self) -> int:
        """Return numeric value for sorting (0=highest priority)."""
        return {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}[self]

    @property
    def display_symbol(self) -> str:
        """Return visual indicator for CLI display."""
        return {Priority.HIGH: "!!!", Priority.MEDIUM: "!!", Priority.LOW: "!"}[self]


@dataclass
class Task:
    """Represents a todo task.

    Attributes:
        id: Unique identifier (auto-assigned by TaskManager)
        title: Brief description of the task (required)
        description: Optional detailed description
        completed: Whether the task is complete (default: False)
        priority: Task priority level (default: Medium)
    """

    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Priority = Priority.MEDIUM
