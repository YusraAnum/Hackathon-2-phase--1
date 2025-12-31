# Quickstart: In-Memory Todo CLI Application

**Feature**: 001-inmemory-todo-cli
**Date**: 2025-12-29

## Prerequisites

- Python 3.13 or higher
- UV package manager (recommended) or pip

## Setup

### 1. Clone and Navigate

```bash
cd "THE EVOLUTION OF TODO APP -PHASE 1"
```

### 2. Create Virtual Environment (UV)

```bash
uv venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
uv pip install -e .
# OR
pip install -e .
```

### 4. Verify Installation

```bash
python --version  # Should show 3.13+
python -c "from src.models.task import Task; print('OK')"
```

## Running the Application

```bash
python main.py
```

### Expected Output

```
=================================
       TODO APPLICATION
=================================

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/unit/test_task.py

# Run with verbose output
pytest -v
```

## Usage Examples

### Adding a Task

```
Enter your choice (1-6): 1

Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread

Task created successfully!
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
```

### Viewing Tasks

```
Enter your choice (1-6): 2

=== Your Tasks ===

[1] [ ] Buy groceries
    Milk, eggs, bread

[2] [x] Call mom
    (no description)

Total: 2 tasks (1 complete, 1 incomplete)
```

### Marking Complete

```
Enter your choice (1-6): 5

Enter task ID to toggle: 1

Task 1 marked as complete!
```

### Updating a Task

```
Enter your choice (1-6): 3

Enter task ID to update: 1
Enter new title (press Enter to keep current): Get groceries
Enter new description (press Enter to keep current):

Task 1 updated successfully!
```

### Deleting a Task

```
Enter your choice (1-6): 4

Enter task ID to delete: 1

Task 1 deleted successfully!
```

### Exiting

```
Enter your choice (1-6): 6

Goodbye!
```

## Project Structure

```
THE EVOLUTION OF TODO APP -PHASE 1/
├── main.py                    # Entry point
├── pyproject.toml             # Project configuration
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py            # Task dataclass
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_manager.py    # Business logic
│   └── cli/
│       ├── __init__.py
│       ├── menu.py            # Menu display
│       ├── handlers.py        # Action handlers
│       └── validators.py      # Input validation
└── tests/
    ├── __init__.py
    ├── unit/
    │   ├── test_task.py
    │   └── test_task_manager.py
    └── integration/
        └── test_cli_flows.py
```

## Common Issues

### Python Version

```
Error: Python 3.13+ required
```

**Solution**: Install Python 3.13 or update your PATH.

### Module Not Found

```
ModuleNotFoundError: No module named 'src'
```

**Solution**: Run `pip install -e .` from project root.

### Permission Denied (Windows)

```
.venv\Scripts\activate : cannot be loaded because running scripts is disabled
```

**Solution**: Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Development Workflow

1. Make changes to source files in `src/`
2. Run tests: `pytest`
3. Test manually: `python main.py`
4. Commit changes following spec-driven workflow

## Notes

- All data is stored in memory and lost when the application exits
- Task IDs are never reused within a session
- This is Phase I - no persistence, single user, console only
