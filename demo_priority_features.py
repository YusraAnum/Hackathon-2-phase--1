"""Demonstration script for priority features in Todo CLI.

This script demonstrates all priority-related functionality including:
- Adding tasks with High, Medium, and Low priorities
- Default priority behavior (Medium)
- Priority-based sorting
- Updating task priorities
- Visual priority indicators
- Integration with completion status

Run this script to see the priority system in action without user input.
For interactive testing, run: python main.py
"""

from src.services.task_manager import TaskManager
from src.models.task import Priority
from src.cli.handlers import format_task_display


def main():
    """Run the priority features demonstration."""

    print("\n" + "="*70)
    print(" TODO CLI - PRIORITY FEATURES DEMONSTRATION")
    print("="*70)

    manager = TaskManager()

    # Scenario 1: Add tasks with different priorities
    print("\n[1] ADDING TASKS WITH DIFFERENT PRIORITIES")
    print("-" * 70)

    task1 = manager.add_task(
        "Fix production bug",
        "Critical issue affecting users",
        Priority.HIGH
    )
    print(f"Added HIGH priority: {task1.title}")

    task2 = manager.add_task(
        "Update documentation",
        "Add API examples",
        Priority.LOW
    )
    print(f"Added LOW priority: {task2.title}")

    task3 = manager.add_task(
        "Review code changes",
        "Pull request #123"
        # Note: Priority defaults to MEDIUM when not specified
    )
    print(f"Added MEDIUM priority (default): {task3.title}")

    task4 = manager.add_task(
        "Deploy to staging",
        "Test new features",
        Priority.HIGH
    )
    print(f"Added HIGH priority: {task4.title}")

    task5 = manager.add_task(
        "Write unit tests",
        "Cover edge cases",
        Priority.MEDIUM
    )
    print(f"Added MEDIUM priority: {task5.title}")

    task6 = manager.add_task(
        "Refactor old code",
        "",
        Priority.LOW
    )
    print(f"Added LOW priority: {task6.title}")

    # Scenario 2: View tasks sorted by priority
    print("\n[2] VIEWING TASKS (SORTED BY PRIORITY)")
    print("-" * 70)
    print("\nPriority Indicators:")
    print("  [!!!] = High priority")
    print("  [!!]  = Medium priority")
    print("  [!]   = Low priority")
    print("\nTask List:\n")

    tasks = manager.get_all_tasks()
    for task in tasks:
        print(format_task_display(task))

    # Display statistics
    high_count = sum(1 for t in tasks if t.priority == Priority.HIGH)
    medium_count = sum(1 for t in tasks if t.priority == Priority.MEDIUM)
    low_count = sum(1 for t in tasks if t.priority == Priority.LOW)

    print(f"Total: {len(tasks)} tasks")
    print(f"  - High priority: {high_count}")
    print(f"  - Medium priority: {medium_count}")
    print(f"  - Low priority: {low_count}")

    # Scenario 3: Mark a task complete
    print("\n[3] MARKING A TASK AS COMPLETE")
    print("-" * 70)

    manager.toggle_complete(task1.id)
    print(f"Marked task #{task1.id} as complete: {task1.title}")

    # Scenario 4: Update task priority
    print("\n[4] UPDATING TASK PRIORITY")
    print("-" * 70)

    print(f"Before: Task #{task2.id} has {task2.priority.value} priority")
    manager.update_task(task2.id, priority=Priority.HIGH)
    updated_task = manager.get_task_by_id(task2.id)
    print(f"After:  Task #{updated_task.id} has {updated_task.priority.value} priority")
    print("\nTask automatically re-sorted by priority!")

    # Scenario 5: View updated list
    print("\n[5] UPDATED TASK LIST")
    print("-" * 70)
    print()

    tasks = manager.get_all_tasks()
    for task in tasks:
        print(format_task_display(task))

    completed = sum(1 for t in tasks if t.completed)
    incomplete = len(tasks) - completed
    print(f"Total: {len(tasks)} tasks ({completed} complete, {incomplete} incomplete)")

    # Scenario 6: Delete a task
    print("\n[6] DELETING A TASK")
    print("-" * 70)

    manager.delete_task(task6.id)
    print(f"Deleted task #{task6.id}: {task6.title}")

    # Final view
    print("\n[7] FINAL TASK LIST")
    print("-" * 70)
    print()

    tasks = manager.get_all_tasks()
    for task in tasks:
        print(format_task_display(task))

    completed = sum(1 for t in tasks if t.completed)
    incomplete = len(tasks) - completed
    print(f"Total: {len(tasks)} tasks ({completed} complete, {incomplete} incomplete)")

    # Summary
    print("\n" + "="*70)
    print(" DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nKey Features Demonstrated:")
    print("  [OK] Adding tasks with High, Medium, and Low priorities")
    print("  [OK] Default priority (Medium) when not specified")
    print("  [OK] Priority-based sorting (High -> Medium -> Low)")
    print("  [OK] Chronological order within each priority level")
    print("  [OK] Visual priority indicators ([!!!] [!!] [!])")
    print("  [OK] Marking tasks as complete")
    print("  [OK] Updating task priorities with automatic re-sorting")
    print("  [OK] Deleting tasks")
    print("\nFor interactive testing, run: python main.py")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
