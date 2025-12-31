"""Entry point for the Todo CLI application."""

import sys

from src.services.task_manager import TaskManager
from src.cli.menu import display_menu, get_user_choice
from src.cli.handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_filter_by_priority,
    handle_update_task,
    handle_delete_task,
    handle_toggle_complete,
)


def main() -> None:
    """Main application entry point.

    Runs the main application loop: displays menu, gets user choice,
    dispatches to appropriate handler, and repeats until exit.
    """
    manager = TaskManager()

    print("\nWelcome to Todo CLI Application!")
    print("All data is stored in memory and will be lost when you exit.")

    while True:
        try:
            display_menu()
            choice = get_user_choice()

            if choice == "1":
                handle_add_task(manager)
            elif choice == "2":
                handle_view_tasks(manager)
            elif choice == "3":
                handle_filter_by_priority(manager)
            elif choice == "4":
                handle_update_task(manager)
            elif choice == "5":
                handle_delete_task(manager)
            elif choice == "6":
                handle_toggle_complete(manager)
            elif choice == "7":
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print("\nInvalid option. Please try again.")

        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            sys.exit(0)
        except EOFError:
            print("\n\nEnd of input. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
