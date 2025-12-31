# Implementation Plan: In-Memory Todo CLI Application

**Branch**: `001-inmemory-todo-cli` | **Date**: 2025-12-29 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-inmemory-todo-cli/spec.md`

## Summary

Build a menu-driven CLI application for managing todo tasks in memory. The application
supports creating, viewing, updating, deleting, and toggling completion status of tasks.
All data is ephemeral and stored only during runtime. The architecture follows clean
separation of concerns with distinct layers for data models, business logic, and CLI
interaction.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (stdlib only for Phase I)
**Storage**: In-memory (Python list/dict)
**Testing**: pytest
**Target Platform**: Cross-platform console (Windows, macOS, Linux)
**Project Type**: Single project
**Performance Goals**: Instant response for all operations (< 100ms)
**Constraints**: No external dependencies, no persistence, single-user session
**Scale/Scope**: Single user, unlimited tasks per session (memory-bound)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Clean & Modular Code | PASS | Separate modules for models, services, and CLI |
| II. Single Responsibility | PASS | Task model (data), TaskManager (logic), CLI (interaction) |
| III. Explicit Data Models | PASS | Task dataclass with type annotations |
| IV. Simple CLI Behavior | PASS | Menu-driven with clear prompts and error messages |
| V. Iterative Specification | PASS | Spec completed and approved before planning |
| VI. Spec-Driven Development | PASS | All features trace to FR-001 through FR-011 |

**Constraints Compliance**:
- No Persistence: PASS - in-memory storage only
- Runtime: PASS - Python 3.13+ required
- Interface: PASS - Console-based only
- Data Lifecycle: PASS - Ephemeral, resets on exit

## Project Structure

### Documentation (this feature)

```text
specs/001-inmemory-todo-cli/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (internal contracts)
│   └── task-manager.md  # TaskManager interface contract
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── models/
│   ├── __init__.py
│   └── task.py          # Task dataclass
├── services/
│   ├── __init__.py
│   └── task_manager.py  # TaskManager class (business logic)
└── cli/
    ├── __init__.py
    ├── menu.py          # Menu display and navigation
    ├── handlers.py      # Action handlers (add, view, update, delete, toggle)
    └── validators.py    # Input validation utilities

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_task.py
│   └── test_task_manager.py
└── integration/
    ├── __init__.py
    └── test_cli_flows.py

main.py                  # Entry point
pyproject.toml           # Project configuration
```

**Structure Decision**: Single project structure selected. This is a standalone CLI
application with no web/mobile components. The three-layer architecture (models,
services, cli) enforces separation of concerns per Constitution Principle II.

## Module Responsibilities

### Layer 1: Models (`src/models/`)

**task.py** - Data definition only
- `Task` dataclass with fields: id, title, description, completed
- No business logic, validation at construction only
- Immutable ID after creation

### Layer 2: Services (`src/services/`)

**task_manager.py** - Business logic layer
- `TaskManager` class managing task collection
- Methods: add_task, get_all_tasks, get_task_by_id, update_task, delete_task, toggle_complete
- ID generation (auto-increment)
- Task lookup and validation (exists/not exists)

### Layer 3: CLI (`src/cli/`)

**menu.py** - User interface
- Display main menu with numbered options
- Get user menu selection
- Main application loop

**handlers.py** - Action coordination
- Handle each menu option
- Prompt for required inputs
- Call TaskManager methods
- Display results/errors

**validators.py** - Input sanitization
- Validate integer input for IDs
- Validate non-empty strings for titles
- Return structured validation results

## Complexity Tracking

> No violations. Design follows constitution principles with minimal complexity.

| Aspect | Decision | Rationale |
|--------|----------|-----------|
| No ORM | Direct in-memory storage | Phase I constraint; no persistence needed |
| No framework | Pure Python stdlib | Simplicity; no external dependencies for Phase I |
| Three layers | models/services/cli | Minimum separation for single responsibility |
