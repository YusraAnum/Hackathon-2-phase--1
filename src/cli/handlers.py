"""CLI action handlers for the Todo application."""

from src.models.task import Task, Priority
from src.services.task_manager import TaskManager
from src.cli.validators import validate_integer, validate_non_empty_string, validate_priority


def format_task_display(task: Task) -> str:
    """Format a single task for display with priority indicator.

    Args:
        task: The task to format

    Returns:
        Formatted string representation: [ID] [PRIORITY] [STATUS] TITLE
                                                          Description
    """
    status = "[x]" if task.completed else "[ ]"
    priority_symbol = f"[{task.priority.display_symbol}]"
    description_line = f"    {task.description}" if task.description else "    (no description)"
    return f"[{task.id}] {priority_symbol} {status} {task.title}\n{description_line}"


def handle_add_task(manager: TaskManager) -> None:
    """Handle the Add Task action.

    Prompts for title, optional description, and optional priority.
    Creates the task and displays confirmation.

    Args:
        manager: The TaskManager instance
    """
    print("\n--- Add New Task ---")

    # Get title
    title = input("Enter task title: ")
    is_valid, stripped_title, error = validate_non_empty_string(title)
    if not is_valid:
        print(f"\nError: {error}")
        return

    # Get description (optional)
    description = input("Enter task description (optional): ")

    # Get priority (optional, defaults to Medium)
    priority_input = input("Enter priority (High/H, Medium/M, Low/L) [default: Medium]: ")
    is_valid, priority, error = validate_priority(priority_input)
    if not is_valid:
        print(f"\nError: {error}")
        return

    # Create task
    try:
        task = manager.add_task(stripped_title, description, priority)
        print(f"\nTask created successfully!")
        print(f"ID: {task.id}")
        print(f"Title: {task.title}")
        print(f"Priority: {task.priority.value}")
        if task.description:
            print(f"Description: {task.description}")
    except ValueError as e:
        print(f"\nError: {e}")


def handle_view_tasks(manager: TaskManager) -> None:
    """Handle the View Tasks action.

    Displays all tasks or a message if no tasks exist.

    Args:
        manager: The TaskManager instance
    """
    print("\n--- Your Tasks ---\n")

    tasks = manager.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(format_task_display(task))
        print()

    # Summary
    completed = sum(1 for t in tasks if t.completed)
    incomplete = len(tasks) - completed
    print(f"Total: {len(tasks)} tasks ({completed} complete, {incomplete} incomplete)")


def handle_filter_by_priority(manager: TaskManager) -> None:
    """Handle the Filter Tasks by Priority action.

    Prompts user for priority level and displays only matching tasks.

    Args:
        manager: The TaskManager instance
    """
    print("\n--- Filter Tasks by Priority ---")

    # Get priority filter
    priority_input = input("\nEnter priority to filter (High/H, Medium/M, Low/L): ")
    is_valid, priority, error = validate_priority(priority_input)

    if not is_valid:
        print(f"\nError: {error}")
        return

    # Get all tasks and filter by priority
    all_tasks = manager.get_all_tasks()
    filtered_tasks = [task for task in all_tasks if task.priority == priority]

    print(f"\n--- Tasks with {priority.value} Priority ---\n")

    if not filtered_tasks:
        print(f"No {priority.value} priority tasks found.")
        return

    for task in filtered_tasks:
        print(format_task_display(task))
        print()

    # Summary
    completed = sum(1 for t in filtered_tasks if t.completed)
    incomplete = len(filtered_tasks) - completed
    print(f"Total: {len(filtered_tasks)} {priority.value} priority tasks "
          f"({completed} complete, {incomplete} incomplete)")


def handle_update_task(manager: TaskManager) -> None:
    """Handle the Update Task action.

    Prompts for task ID and allows updating title, description, and/or priority.
    Displays confirmation after update.

    Args:
        manager: The TaskManager instance
    """
    print("\n--- Update Task ---")

    # Get task ID
    id_input = input("Enter task ID to update: ")
    is_valid, task_id, error = validate_integer(id_input)
    if not is_valid:
        print(f"\nError: {error}")
        return

    # Check if task exists
    task = manager.get_task_by_id(task_id)
    if task is None:
        print("\nError: Task not found.")
        return

    # Show current values
    print(f"\nCurrent title: {task.title}")
    print(f"Current description: {task.description or '(empty)'}")
    print(f"Current priority: {task.priority.value}")

    # Get new title
    new_title_input = input("\nEnter new title (press Enter to keep current): ")
    new_title = new_title_input.strip() if new_title_input.strip() else None

    # Validate new title if provided
    if new_title is not None:
        is_valid, _, error = validate_non_empty_string(new_title)
        if not is_valid:
            print(f"\nError: {error}")
            return

    # Get new description
    new_desc_input = input("Enter new description (press Enter to keep current): ")
    new_description = new_desc_input if new_desc_input else None

    # Get new priority
    new_priority_input = input(
        "Enter new priority (High/H, Medium/M, Low/L, press Enter to keep current): "
    )
    new_priority = None
    if new_priority_input.strip():  # Only validate if user entered something
        is_valid, new_priority, error = validate_priority(new_priority_input)
        if not is_valid:
            print(f"\nError: {error}")
            return

    # Update task
    try:
        updated = manager.update_task(
            task_id, title=new_title, description=new_description, priority=new_priority
        )
        if updated:
            print(f"\nTask {task_id} updated successfully!")
        else:
            print("\nError: Task not found.")
    except ValueError as e:
        print(f"\nError: {e}")


def handle_delete_task(manager: TaskManager) -> None:
    """Handle the Delete Task action.

    Prompts for task ID, deletes the task, and displays confirmation.

    Args:
        manager: The TaskManager instance
    """
    print("\n--- Delete Task ---")

    # Get task ID
    id_input = input("Enter task ID to delete: ")
    is_valid, task_id, error = validate_integer(id_input)
    if not is_valid:
        print(f"\nError: {error}")
        return

    # Delete task
    if manager.delete_task(task_id):
        print(f"\nTask {task_id} deleted successfully!")
    else:
        print("\nError: Task not found.")


def handle_toggle_complete(manager: TaskManager) -> None:
    """Handle the Mark Complete/Incomplete action.

    Prompts for task ID, toggles completion status, and displays confirmation.

    Args:
        manager: The TaskManager instance
    """
    print("\n--- Mark Complete/Incomplete ---")

    # Get task ID
    id_input = input("Enter task ID to toggle: ")
    is_valid, task_id, error = validate_integer(id_input)
    if not is_valid:
        print(f"\nError: {error}")
        return

    # Toggle task
    task = manager.toggle_complete(task_id)
    if task:
        status = "complete" if task.completed else "incomplete"
        print(f"\nTask {task_id} marked as {status}!")
    else:
        print("\nError: Task not found.")
