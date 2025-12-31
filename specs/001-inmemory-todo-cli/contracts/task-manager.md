# Contract: TaskManager Service

**Feature**: 001-inmemory-todo-cli
**Date**: 2025-12-29
**Module**: `src/services/task_manager.py`

## Overview

TaskManager is the service layer responsible for all task business logic. It manages
the in-memory task collection and provides methods for CRUD operations plus status
toggling. The CLI layer interacts exclusively through this interface.

## Interface Definition

```python
class TaskManager:
    """Manages task collection and business operations."""

    def add_task(self, title: str, description: str = "") -> Task:
        """Create a new task with auto-generated ID.

        Args:
            title: Task title (required, non-empty)
            description: Optional task description

        Returns:
            The created Task instance

        Raises:
            ValueError: If title is empty or whitespace-only
        """

    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks.

        Returns:
            List of all tasks, ordered by ID (ascending)
        """

    def get_task_by_id(self, task_id: int) -> Task | None:
        """Retrieve a single task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task if found, None otherwise
        """

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        description: str | None = None
    ) -> Task | None:
        """Update an existing task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (if provided and not None)
            description: New description (if provided and not None)

        Returns:
            The updated Task if found, None if task doesn't exist

        Raises:
            ValueError: If title is provided but empty/whitespace-only
        """

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """

    def toggle_complete(self, task_id: int) -> Task | None:
        """Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task if found, None if task doesn't exist
        """

    def task_count(self) -> int:
        """Get the total number of tasks.

        Returns:
            Number of tasks currently stored
        """
```

## Method Contracts

### add_task

| Aspect | Specification |
|--------|---------------|
| Precondition | title is non-empty string after stripping whitespace |
| Postcondition | Task created with unique ID, stored in collection |
| Side Effects | Increments internal ID counter |
| Idempotent | No - each call creates a new task |
| Error Handling | Raises ValueError for invalid title |

**Example**:
```python
manager = TaskManager()
task = manager.add_task("Buy milk", "2% milk from store")
assert task.id == 1
assert task.title == "Buy milk"
assert task.completed is False
```

### get_all_tasks

| Aspect | Specification |
|--------|---------------|
| Precondition | None |
| Postcondition | Returns list of all tasks |
| Side Effects | None |
| Idempotent | Yes |
| Error Handling | Returns empty list if no tasks |

**Example**:
```python
manager = TaskManager()
tasks = manager.get_all_tasks()
assert tasks == []

manager.add_task("Task 1")
manager.add_task("Task 2")
tasks = manager.get_all_tasks()
assert len(tasks) == 2
```

### get_task_by_id

| Aspect | Specification |
|--------|---------------|
| Precondition | task_id is integer |
| Postcondition | Returns task if exists, None otherwise |
| Side Effects | None |
| Idempotent | Yes |
| Error Handling | Returns None for non-existent ID |

**Example**:
```python
manager = TaskManager()
task = manager.add_task("Test")

found = manager.get_task_by_id(1)
assert found is not None
assert found.title == "Test"

not_found = manager.get_task_by_id(999)
assert not_found is None
```

### update_task

| Aspect | Specification |
|--------|---------------|
| Precondition | task_id is integer; if title provided, must be non-empty |
| Postcondition | Task fields updated if task exists |
| Side Effects | Modifies existing task in collection |
| Idempotent | Yes (same inputs produce same result) |
| Error Handling | Returns None if not found; raises ValueError for empty title |

**Example**:
```python
manager = TaskManager()
manager.add_task("Original", "Old description")

updated = manager.update_task(1, title="New Title")
assert updated.title == "New Title"
assert updated.description == "Old description"  # Unchanged

updated = manager.update_task(1, description="New description")
assert updated.title == "New Title"  # Unchanged
assert updated.description == "New description"
```

### delete_task

| Aspect | Specification |
|--------|---------------|
| Precondition | task_id is integer |
| Postcondition | Task removed from collection if existed |
| Side Effects | Removes task from storage |
| Idempotent | Yes (deleting non-existent returns False) |
| Error Handling | Returns False if task not found |

**Example**:
```python
manager = TaskManager()
manager.add_task("To Delete")

result = manager.delete_task(1)
assert result is True
assert manager.get_task_by_id(1) is None

result = manager.delete_task(1)  # Already deleted
assert result is False
```

### toggle_complete

| Aspect | Specification |
|--------|---------------|
| Precondition | task_id is integer |
| Postcondition | Task.completed flipped if task exists |
| Side Effects | Modifies existing task in collection |
| Idempotent | No - each call flips the state |
| Error Handling | Returns None if task not found |

**Example**:
```python
manager = TaskManager()
task = manager.add_task("Toggle Me")
assert task.completed is False

toggled = manager.toggle_complete(1)
assert toggled.completed is True

toggled = manager.toggle_complete(1)
assert toggled.completed is False
```

## Error Taxonomy

| Error | Condition | Response |
|-------|-----------|----------|
| Task Not Found | ID doesn't exist in collection | Return None or False |
| Empty Title | Title is "" or whitespace only | Raise ValueError |
| Invalid ID Type | Non-integer ID (caught at caller) | Type error (prevented by type hints) |

## Invariants

1. **ID Uniqueness**: No two tasks share the same ID at any point
2. **ID Monotonicity**: IDs always increase; never decrease or repeat
3. **Title Non-Empty**: All stored tasks have non-empty titles
4. **Collection Consistency**: get_all_tasks returns exactly what's stored
