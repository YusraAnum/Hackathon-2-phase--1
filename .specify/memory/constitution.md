<!--
SYNC IMPACT REPORT
==================
Version change: 0.0.0 → 1.0.0
Change type: MAJOR - Initial ratification of project constitution

Added Principles:
- I. Clean & Modular Code
- II. Single Responsibility
- III. Explicit Data Models
- IV. Simple CLI Behavior
- V. Iterative Specification
- VI. Spec-Driven Development

Added Sections:
- Core Principles (6 principles)
- Constraints (Phase I limitations)
- Tooling & Workflow

Templates requiring updates:
- ✅ plan-template.md - Constitution Check section compatible (gates determined dynamically)
- ✅ spec-template.md - Requirements align with explicit data models principle
- ✅ tasks-template.md - Task phases compatible with iterative improvement principle

Follow-up TODOs: None
==================
-->

# Todo Evolution Constitution

## Core Principles

### I. Clean & Modular Code

All code MUST be clean, readable, and organized into logical modules. Code clarity takes
precedence over clever optimizations. Each module MUST have a clear purpose and well-defined
boundaries. Naming conventions MUST be consistent and self-documenting.

**Rationale**: Maintainability and onboarding efficiency require code that communicates intent
without extensive documentation.

### II. Single Responsibility

Every module, class, and function MUST have a single, well-defined responsibility. A module
MUST NOT mix concerns (e.g., data access with business logic, or CLI parsing with domain rules).
When a component grows beyond its original purpose, it MUST be refactored into separate units.

**Rationale**: Single responsibility enables independent testing, easier debugging, and focused
changes that minimize unintended side effects.

### III. Explicit Data Models

All data structures MUST be explicitly defined with clear type annotations. Domain entities MUST
be modeled as dedicated classes or dataclasses—not ad-hoc dictionaries. Data validation MUST
occur at model boundaries. No implicit data transformations are permitted.

**Rationale**: Explicit models catch errors early, improve IDE support, and serve as living
documentation of the domain.

### IV. Simple CLI Behavior

The CLI interface MUST be simple and predictable. Commands MUST follow standard conventions
(--help, exit codes, stderr for errors). Output MUST be human-readable by default. The CLI MUST
provide clear feedback for all operations—success, failure, and validation errors.

**Rationale**: Predictable CLI behavior reduces user friction and enables reliable scripting
and automation.

### V. Iterative Specification

Features evolve through specification versioning. Each iteration MUST be documented with clear
acceptance criteria before implementation begins. Specifications MUST be updated when requirements
change—never implement undocumented changes. Small, incremental improvements are preferred over
large rewrites.

**Rationale**: Iterative specification maintains traceability, enables course correction, and
prevents scope creep.

### VI. Spec-Driven Development

Spec-driven development is MANDATORY. No implementation begins without a corresponding
specification. The specification is the source of truth for feature behavior. All code MUST
trace back to documented requirements. Manual boilerplate is prohibited—all implementation
is generated using Claude Code and Spec-Kit Plus.

**Rationale**: Spec-driven development ensures alignment between intent and implementation,
enables AI-assisted generation, and maintains architectural consistency.

## Constraints

Phase I of Todo Evolution operates under strict constraints to focus on core functionality:

- **No Persistence**: No databases, files, or external storage. All data is in-memory only.
- **Runtime**: Python 3.13+ is required.
- **Interface**: Console-based interaction only—no web UI, API, or GUI.
- **Data Lifecycle**: All data is ephemeral; application state resets on restart.

These constraints WILL be lifted in subsequent phases as the system evolves.

## Tooling & Workflow

The project uses the following tooling stack:

- **UV**: Environment and dependency management
- **Claude Code**: AI-assisted implementation and code generation
- **Spec-Kit Plus**: Specification-driven workflows (/sp.specify, /sp.plan, /sp.tasks, etc.)

**Workflow Requirements**:
1. Human role is limited to product architect, reviewer, and spec author
2. Implementation is generated—not manually written
3. All changes flow through the spec → plan → tasks pipeline
4. PHRs (Prompt History Records) document all significant interactions
5. ADRs (Architecture Decision Records) capture significant decisions

## Governance

This constitution supersedes all other project practices. Amendments require:

1. Documentation of the proposed change
2. Review and approval by the project maintainer
3. Version increment following semantic versioning:
   - MAJOR: Principle removal or incompatible redefinition
   - MINOR: New principle or section addition
   - PATCH: Clarifications and non-semantic refinements
4. Update of all dependent artifacts (templates, docs)

**Compliance**: All PRs and reviews MUST verify adherence to these principles. Constitution
violations MUST be resolved before merge.

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29
