# Research: In-Memory Todo CLI Application

**Feature**: 001-inmemory-todo-cli
**Date**: 2025-12-29
**Status**: Complete

## Research Summary

This document captures technical decisions and rationale for the In-Memory Todo CLI
implementation. Given the Phase I constraints (Python 3.13+, stdlib only, in-memory),
most decisions are straightforward with minimal alternatives to evaluate.

## Decision 1: Data Model Implementation

**Decision**: Use Python `dataclass` with `field()` defaults

**Rationale**:
- Native Python 3.13+ feature, no external dependencies
- Automatic `__init__`, `__repr__`, `__eq__` generation
- Type annotations enforced by dataclass decorator
- Immutable fields supported via `frozen=True` if needed

**Alternatives Considered**:
| Option | Pros | Cons | Rejected Because |
|--------|------|------|------------------|
| Plain class | Full control | Boilerplate for __init__, __repr__ | Violates clean code principle |
| NamedTuple | Immutable | No default values, awkward updates | Tasks need mutable completion status |
| TypedDict | Dict-like access | No validation, implicit structure | Violates explicit data models principle |
| Pydantic | Rich validation | External dependency | Phase I constraint: stdlib only |

## Decision 2: Task Storage Structure

**Decision**: Use a Python `dict` with task ID as key

**Rationale**:
- O(1) lookup by ID for get, update, delete operations
- O(n) iteration for list all (acceptable for in-memory scale)
- Simple deletion without index shifting
- ID uniqueness enforced by dict key semantics

**Alternatives Considered**:
| Option | Pros | Cons | Rejected Because |
|--------|------|------|------------------|
| List | Ordered, simple | O(n) lookup by ID | Inefficient for ID-based operations |
| OrderedDict | Ordered + O(1) lookup | Slightly more complex | Dict in Python 3.7+ maintains insertion order |

## Decision 3: ID Generation Strategy

**Decision**: Auto-incrementing integer starting at 1, never reused

**Rationale**:
- Simple, predictable for users
- Unique across session regardless of deletions
- Matches spec requirement FR-002

**Implementation**:
```python
class TaskManager:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
```

## Decision 4: CLI Input Handling

**Decision**: Use built-in `input()` with custom validation functions

**Rationale**:
- No external dependencies
- Simple, testable validation layer
- Clear separation between input collection and validation

**Alternatives Considered**:
| Option | Pros | Cons | Rejected Because |
|--------|------|------|------------------|
| argparse | Standard CLI parsing | Designed for args, not interactive menus | Menu-driven, not command-line args |
| click | Rich CLI features | External dependency | Phase I constraint |
| prompt_toolkit | Advanced input features | External dependency | Phase I constraint |

## Decision 5: Error Handling Strategy

**Decision**: Return-based error handling with dedicated result types

**Rationale**:
- Explicit error paths without exceptions for expected failures
- Exceptions reserved for unexpected/programming errors
- Clean separation between "not found" (expected) and "system error" (unexpected)

**Pattern**:
```python
def get_task_by_id(self, task_id: int) -> Task | None:
    return self._tasks.get(task_id)

# Caller handles None case explicitly
task = manager.get_task_by_id(user_id)
if task is None:
    print("Task not found.")
```

## Decision 6: Module Organization

**Decision**: Three-layer architecture (models → services → cli)

**Rationale**:
- Enforces single responsibility (Constitution Principle II)
- Models have no dependencies
- Services depend only on models
- CLI depends on services and models
- Clear import hierarchy prevents circular dependencies

**Dependency Graph**:
```
cli/
  ├── handlers.py → services/task_manager.py → models/task.py
  ├── menu.py → handlers.py
  └── validators.py (no internal dependencies)
```

## Open Questions Resolved

All technical questions from the spec have been resolved:

| Question | Resolution |
|----------|------------|
| How to store tasks? | Dict with ID keys |
| How to generate IDs? | Auto-increment, never reuse |
| How to handle invalid input? | Validation functions + clear error messages |
| How to structure code? | Three-layer: models/services/cli |
| What testing framework? | pytest (standard choice for Python) |

## Next Steps

1. Proceed to Phase 1: Generate data-model.md with entity details
2. Generate contracts/ with TaskManager interface
3. Generate quickstart.md for developer setup
