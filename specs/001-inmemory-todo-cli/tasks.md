# Tasks: In-Memory Todo CLI Application

**Input**: Design documents from `/specs/001-inmemory-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/task-manager.md

**Tests**: Not explicitly requested in spec. Test tasks omitted.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Create project structure and configuration

- [x] T001 Create project directory structure per plan.md (src/, src/models/, src/services/, src/cli/, tests/)
- [x] T002 [P] Create pyproject.toml with Python 3.13+ requirement and project metadata
- [x] T003 [P] Create src/__init__.py with package initialization
- [x] T004 [P] Create src/models/__init__.py
- [x] T005 [P] Create src/services/__init__.py
- [x] T006 [P] Create src/cli/__init__.py
- [x] T007 [P] Create tests/__init__.py
- [x] T008 Create main.py entry point stub (empty main function)

**Checkpoint**: Project structure ready - can import from src package

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T009 Implement Task dataclass in src/models/task.py per data-model.md
- [x] T010 Create TaskManager class skeleton in src/services/task_manager.py with __init__ and _next_id
- [x] T011 [P] Create validators.py in src/cli/validators.py with validate_integer() and validate_non_empty_string()
- [x] T012 [P] Create menu.py skeleton in src/cli/menu.py with display_menu() and get_user_choice()

**Checkpoint**: Foundation ready - Task model exists, TaskManager can be instantiated

---

## Phase 3: User Story 1 - Add a New Task (Priority: P1)

**Goal**: Users can add tasks with title and optional description

**Independent Test**: Launch app → Select "Add Task" → Enter title → Verify task created with unique ID

### Implementation for User Story 1

- [x] T013 [US1] Implement TaskManager.add_task() method in src/services/task_manager.py
- [x] T014 [US1] Implement handle_add_task() in src/cli/handlers.py (prompt title, description, call add_task, display result)
- [x] T015 [US1] Add "Add Task" option (option 1) to menu in src/cli/menu.py
- [x] T016 [US1] Wire handle_add_task to menu option 1 in main.py application loop

**Checkpoint**: User Story 1 complete - can add tasks and see confirmation

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Users can see all tasks with ID, title, description, and status

**Independent Test**: Add sample tasks → Select "View Tasks" → Verify all tasks displayed correctly

### Implementation for User Story 2

- [x] T017 [US2] Implement TaskManager.get_all_tasks() method in src/services/task_manager.py
- [x] T018 [US2] Implement format_task_display() helper in src/cli/handlers.py for single task formatting
- [x] T019 [US2] Implement handle_view_tasks() in src/cli/handlers.py (get tasks, format, display or "No tasks")
- [x] T020 [US2] Add "View Tasks" option (option 2) to menu in src/cli/menu.py
- [x] T021 [US2] Wire handle_view_tasks to menu option 2 in main.py application loop

**Checkpoint**: User Stories 1 & 2 complete - MVP functional (add + view)

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle a task's completion status by ID

**Independent Test**: Add task → Toggle status → View task → Verify status changed

### Implementation for User Story 3

- [x] T022 [US3] Implement TaskManager.get_task_by_id() method in src/services/task_manager.py
- [x] T023 [US3] Implement TaskManager.toggle_complete() method in src/services/task_manager.py
- [x] T024 [US3] Implement handle_toggle_complete() in src/cli/handlers.py (prompt ID, validate, toggle, display result/error)
- [x] T025 [US3] Add "Mark Complete/Incomplete" option (option 5) to menu in src/cli/menu.py
- [x] T026 [US3] Wire handle_toggle_complete to menu option 5 in main.py application loop

**Checkpoint**: User Story 3 complete - can track task progress

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Users can update a task's title and/or description by ID

**Independent Test**: Add task → Update title/description → View task → Verify changes

### Implementation for User Story 4

- [x] T027 [US4] Implement TaskManager.update_task() method in src/services/task_manager.py
- [x] T028 [US4] Implement handle_update_task() in src/cli/handlers.py (prompt ID, prompt new values, update, display result/error)
- [x] T029 [US4] Add "Update Task" option (option 3) to menu in src/cli/menu.py
- [x] T030 [US4] Wire handle_update_task to menu option 3 in main.py application loop

**Checkpoint**: User Story 4 complete - can edit tasks

---

## Phase 7: User Story 5 - Delete a Task (Priority: P3)

**Goal**: Users can remove tasks they no longer need

**Independent Test**: Add task → Delete by ID → View tasks → Verify task removed

### Implementation for User Story 5

- [x] T031 [US5] Implement TaskManager.delete_task() method in src/services/task_manager.py
- [x] T032 [US5] Implement handle_delete_task() in src/cli/handlers.py (prompt ID, validate, delete, display result/error)
- [x] T033 [US5] Add "Delete Task" option (option 4) to menu in src/cli/menu.py
- [x] T034 [US5] Wire handle_delete_task to menu option 4 in main.py application loop

**Checkpoint**: User Story 5 complete - full CRUD functionality

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final integration and edge case handling

- [x] T035 Add "Exit" option (option 6) to menu with graceful shutdown in src/cli/menu.py
- [x] T036 Implement main application loop in main.py (display menu, get choice, dispatch to handler, repeat until exit)
- [x] T037 Add error handling for invalid menu options in main.py
- [x] T038 Add graceful handling of KeyboardInterrupt (Ctrl+C) in main.py
- [x] T039 Verify all edge cases from spec: empty title, whitespace title, non-integer ID, non-existent ID
- [x] T040 Run quickstart.md validation - verify all usage examples work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup ──────────────────────────► (no dependencies)
                    │
                    ▼
Phase 2: Foundational ──────────────────► depends on Phase 1
                    │
         ┌──────────┼──────────┐
         ▼          ▼          ▼
Phase 3: US1    Phase 4: US2   (P1 stories can run in parallel after Phase 2)
         │          │
         ▼          ▼
Phase 5: US3    Phase 6: US4   (P2 stories can run in parallel, need US1 for testing)
         │          │
         └────┬─────┘
              ▼
Phase 7: US5 ──────────────────────────► (P3 story, can follow any P2)
              │
              ▼
Phase 8: Polish ───────────────────────► depends on all user stories
```

### User Story Dependencies

| Story | Depends On | Reason |
|-------|------------|--------|
| US1 (Add) | Foundational | Needs Task model and TaskManager |
| US2 (View) | Foundational | Needs Task model and TaskManager |
| US3 (Toggle) | US1 | Needs tasks to exist to toggle |
| US4 (Update) | US1 | Needs tasks to exist to update |
| US5 (Delete) | US1 | Needs tasks to exist to delete |

### Within Each User Story

1. TaskManager method(s) first
2. CLI handler(s) second
3. Menu option(s) third
4. Wire to main.py last

### Parallel Opportunities

**Phase 1 parallel tasks**: T002, T003, T004, T005, T006, T007
**Phase 2 parallel tasks**: T011, T012
**US1 + US2 can run in parallel** (both are P1, independent)
**US3 + US4 can run in parallel** (both are P2, independent)

---

## Parallel Example: Phase 1 Setup

```bash
# Launch all init files in parallel:
Task: "Create pyproject.toml with Python 3.13+ requirement"
Task: "Create src/__init__.py with package initialization"
Task: "Create src/models/__init__.py"
Task: "Create src/services/__init__.py"
Task: "Create src/cli/__init__.py"
Task: "Create tests/__init__.py"
```

## Parallel Example: User Stories 1 & 2

```bash
# After Phase 2 Foundational completes, US1 and US2 can run in parallel:

# Thread A - User Story 1:
Task: "T013 [US1] Implement TaskManager.add_task() method"
Task: "T014 [US1] Implement handle_add_task() handler"
Task: "T015 [US1] Add 'Add Task' option to menu"
Task: "T016 [US1] Wire handle_add_task to menu"

# Thread B - User Story 2:
Task: "T017 [US2] Implement TaskManager.get_all_tasks() method"
Task: "T018 [US2] Implement format_task_display() helper"
Task: "T019 [US2] Implement handle_view_tasks() handler"
Task: "T020 [US2] Add 'View Tasks' option to menu"
Task: "T021 [US2] Wire handle_view_tasks to menu"
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test US1 + US2 independently
6. Deploy/demo if ready - **This is your MVP!**

### Incremental Delivery

| Increment | Adds | Cumulative Features |
|-----------|------|---------------------|
| MVP | US1 + US2 | Add tasks, view tasks |
| +US3 | Toggle complete | Add, view, mark complete |
| +US4 | Update tasks | Add, view, complete, update |
| +US5 | Delete tasks | Full CRUD |
| +Polish | Edge cases, exit | Production-ready |

### Single Developer Flow

1. Phase 1 (Setup) → Phase 2 (Foundation)
2. Phase 3 (US1) → Test adding works
3. Phase 4 (US2) → Test viewing works → **MVP complete**
4. Phase 5 (US3) → Test toggling works
5. Phase 6 (US4) → Test updating works
6. Phase 7 (US5) → Test deleting works
7. Phase 8 (Polish) → Test edge cases → **Done**

---

## Task Summary

| Phase | Task Count | Stories Covered |
|-------|------------|-----------------|
| Setup | 8 | - |
| Foundational | 4 | - |
| US1 (Add) | 4 | P1 |
| US2 (View) | 5 | P1 |
| US3 (Toggle) | 5 | P2 |
| US4 (Update) | 4 | P2 |
| US5 (Delete) | 4 | P3 |
| Polish | 6 | - |
| **Total** | **40** | **5 stories** |

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Menu options: 1=Add, 2=View, 3=Update, 4=Delete, 5=Toggle, 6=Exit
