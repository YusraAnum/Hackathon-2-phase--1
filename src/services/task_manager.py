"""TaskManager service for business logic operations."""

from src.models.task import Task, Priority


class TaskManager:
    """Manages task collection and business operations."""

    def __init__(self) -> None:
        """Initialize the TaskManager with empty task storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(
        self, title: str, description: str = "", priority: Priority = Priority.MEDIUM
    ) -> Task:
        """Create a new task with auto-generated ID.

        Args:
            title: Task title (required, non-empty)
            description: Optional task description
            priority: Task priority level (default: Medium)

        Returns:
            The created Task instance

        Raises:
            ValueError: If title is empty or whitespace-only
        """
        stripped_title = title.strip()
        if not stripped_title:
            raise ValueError("Title cannot be empty or whitespace only")

        task = Task(
            id=self._next_id,
            title=stripped_title,
            description=description.strip(),
            completed=False,
            priority=priority,
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks.

        Returns:
            List of tasks, sorted by priority (High→Medium→Low),
            then by ID (ascending) within each priority level
        """
        return sorted(self._tasks.values(), key=lambda t: (t.priority.sort_order, t.id))

    def get_task_by_id(self, task_id: int) -> Task | None:
        """Retrieve a single task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update_task(
        self,
        task_id: int,
        title: str | None = None,
        description: str | None = None,
        priority: Priority | None = None,
    ) -> Task | None:
        """Update an existing task's title, description, and/or priority.

        Args:
            task_id: The ID of the task to update
            title: New title (if provided and not None)
            description: New description (if provided and not None)
            priority: New priority (if provided and not None)

        Returns:
            The updated Task if found, None if task doesn't exist

        Raises:
            ValueError: If title is provided but empty/whitespace-only
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None

        if title is not None:
            stripped_title = title.strip()
            if not stripped_title:
                raise ValueError("Title cannot be empty or whitespace only")
            task.title = stripped_title

        if description is not None:
            task.description = description.strip()

        if priority is not None:
            task.priority = priority

        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_complete(self, task_id: int) -> Task | None:
        """Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            The updated Task if found, None if task doesn't exist
        """
        task = self._tasks.get(task_id)
        if task is None:
            return None

        task.completed = not task.completed
        return task

    def task_count(self) -> int:
        """Get the total number of tasks.

        Returns:
            Number of tasks currently stored
        """
        return len(self._tasks)
