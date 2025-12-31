# The Evolution of Todo App - Phase 1

A command-line todo application built with Python that demonstrates clean architecture and test-driven development principles. This is Phase 1 of the Todo App Evolution project, featuring in-memory task management.

## Features

- **Add Tasks**: Create new tasks with title, optional description, and priority level
- **Priority Levels**: Organize tasks with High, Medium, or Low priority
- **Smart Sorting**: Tasks automatically sorted by priority, then by creation order
- **View Tasks**: Display all tasks with priority indicators and completion status
- **Filter by Priority**: View only High, Medium, or Low priority tasks
- **Update Tasks**: Modify task titles, descriptions, and priorities
- **Delete Tasks**: Remove tasks you no longer need
- **Toggle Completion**: Mark tasks as complete or incomplete
- **Menu-Driven Interface**: Simple numbered menu for easy navigation
- **Input Validation**: Robust error handling for invalid inputs

## Project Structure

```
THE EVOLUTION OF TODO APP -PHASE 1/
├── src/
│   ├── models/          # Data models (Task)
│   ├── services/        # Business logic (TaskManager)
│   └── cli/             # User interface (menu, handlers, validators)
├── tests/
│   ├── unit/            # Unit tests
│   └── integration/     # Integration tests
├── specs/               # Feature specifications and documentation
├── main.py              # Application entry point
├── pyproject.toml       # Project configuration
└── README.md            # This file
```

## Requirements

- Python 3.13 or higher
- No external dependencies required for core functionality

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YusraAnum/Hackathon-2-phase--1.git
cd Hackathon-2-phase--1
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

Once the application starts, you'll see a menu with the following options:

1. **Add Task** - Create a new task
2. **View Tasks** - Display all tasks
3. **Filter Tasks by Priority** - View only High, Medium, or Low priority tasks
4. **Update Task** - Modify an existing task
5. **Delete Task** - Remove a task
6. **Mark Complete/Incomplete** - Toggle task completion status
7. **Exit** - Close the application

### Example Session

```
Welcome to Todo CLI Application!
All data is stored in memory and will be lost when you exit.

=== Todo CLI Menu ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6): 1

Enter task title: Buy groceries
Enter task description (optional): Get milk, eggs, and bread
Enter priority (High/H, Medium/M, Low/L) [default: Medium]: H

Task created successfully!
ID: 1
Title: Buy groceries
Priority: High
Description: Get milk, eggs, and bread

Enter your choice (1-6): 2

--- Your Tasks ---

[1] [!!!] [ ] Buy groceries
    Get milk, eggs, and bread

Total: 1 tasks (0 complete, 1 incomplete)
```

**Priority Indicators:**
- `[!!!]` = High priority
- `[!!]` = Medium priority
- `[!]` = Low priority

## Architecture

This project follows clean architecture principles:

- **Models Layer** (`src/models/`): Defines the Task entity with validation
- **Services Layer** (`src/services/`): Contains TaskManager for business logic
- **CLI Layer** (`src/cli/`): Handles user interaction and input validation

### Key Components

- **Task**: Data class representing a todo item with id, title, description, and completion status
- **TaskManager**: Manages task storage and operations (CRUD + toggle completion)
- **Menu System**: User-friendly interface with input validation and error handling
- **Validators**: Input validation for task IDs and required fields

## Testing

The project includes comprehensive test coverage for both unit and integration testing.

Run tests (when test framework is configured):
```bash
pytest tests/
```

## Design Decisions

### In-Memory Storage
Phase 1 uses in-memory storage with Python dictionaries. Data is lost when the application exits. This provides:
- Fast operations (O(1) lookups)
- Simple implementation
- Foundation for future database integration in Phase 2

### Auto-Incrementing IDs
Tasks receive sequential integer IDs (1, 2, 3, ...). Deleted IDs are not reused within a session, ensuring referential integrity.

### Priority-Based Sorting
Tasks are automatically sorted by priority level (High → Medium → Low), with chronological ordering (by ID) preserved within each priority group. This ensures important tasks always appear first while maintaining the order tasks were created.

### Menu-Driven Interface
A numbered menu system provides:
- Easy navigation
- Clear user feedback
- Graceful error handling

## Documentation

Detailed documentation is available in the `specs/` directory:

- **spec.md**: Feature specification with user stories and acceptance criteria
- **plan.md**: Architecture decisions and implementation plan
- **tasks.md**: Task breakdown and implementation checklist
- **data-model.md**: Data structures and relationships
- **contracts/**: API contracts for TaskManager

## Limitations (Phase 1)

- **No Persistence**: Data is stored in memory only and lost on exit
- **Single Session**: No multi-user support or concurrent access
- **Basic Features**: No categories, tags, due dates, or advanced search functionality
- **Console Only**: No GUI or web interface

These limitations will be addressed in future phases of the project.

## Future Enhancements

Planned features for future phases:
- Phase 2: File-based persistence
- Phase 3: Database integration
- Phase 4: Categories, tags, and advanced filtering
- Phase 5: Web interface
- Additional: Due dates, reminders, and recurring tasks

## Contributing

This project follows Spec-Driven Development (SDD) methodology. All features are:
1. Specified in detail before implementation
2. Planned with architectural decisions documented
3. Implemented with test coverage
4. Tracked in prompt history records (PHR)

## License

MIT License - see project configuration for details

## Author

YusraAnum - [GitHub Profile](https://github.com/YusraAnum)

## Acknowledgments

Built as part of Hackathon 2 - demonstrating clean architecture, TDD, and professional software development practices
