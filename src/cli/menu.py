"""Menu display and navigation for the CLI."""

MENU_OPTIONS = """
=================================
       TODO APPLICATION
=================================

1. Add Task
2. View Tasks
3. Filter Tasks by Priority
4. Update Task
5. Delete Task
6. Mark Complete/Incomplete
7. Exit

"""


def display_menu() -> None:
    """Display the main menu options."""
    print(MENU_OPTIONS)


def get_user_choice() -> str:
    """Get the user's menu selection.

    Returns:
        The user's input as a string
    """
    return input("Enter your choice (1-7): ").strip()
