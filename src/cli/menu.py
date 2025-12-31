"""Menu display and navigation for the CLI."""

MENU_OPTIONS = """
=================================
       TODO APPLICATION
=================================

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

"""


def display_menu() -> None:
    """Display the main menu options."""
    print(MENU_OPTIONS)


def get_user_choice() -> str:
    """Get the user's menu selection.

    Returns:
        The user's input as a string
    """
    return input("Enter your choice (1-6): ").strip()
