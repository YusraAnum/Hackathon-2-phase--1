"""CLI interface for the Todo application."""

from src.cli.menu import display_menu, get_user_choice
from src.cli.handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_filter_by_priority,
    handle_update_task,
    handle_delete_task,
    handle_toggle_complete,
)
from src.cli.validators import validate_integer, validate_non_empty_string, validate_priority

__all__ = [
    "display_menu",
    "get_user_choice",
    "handle_add_task",
    "handle_view_tasks",
    "handle_filter_by_priority",
    "handle_update_task",
    "handle_delete_task",
    "handle_toggle_complete",
    "validate_integer",
    "validate_non_empty_string",
    "validate_priority",
]
