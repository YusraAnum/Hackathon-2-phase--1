"""Input validation utilities for the CLI."""

from src.models.task import Priority


def validate_integer(value: str) -> tuple[bool, int | None, str]:
    """Validate that a string can be converted to an integer.

    Args:
        value: The string to validate

    Returns:
        A tuple of (is_valid, parsed_value, error_message)
        - is_valid: True if the value is a valid integer
        - parsed_value: The integer value if valid, None otherwise
        - error_message: Empty string if valid, error description otherwise
    """
    try:
        parsed = int(value.strip())
        return True, parsed, ""
    except ValueError:
        return False, None, "Invalid input. Please enter a valid task ID."


def validate_non_empty_string(value: str) -> tuple[bool, str, str]:
    """Validate that a string is non-empty after stripping whitespace.

    Args:
        value: The string to validate

    Returns:
        A tuple of (is_valid, stripped_value, error_message)
        - is_valid: True if the value is non-empty
        - stripped_value: The stripped string value
        - error_message: Empty string if valid, error description otherwise
    """
    stripped = value.strip()
    if not stripped:
        return False, "", "Title cannot be empty or whitespace only."
    return True, stripped, ""


def validate_priority(value: str) -> tuple[bool, Priority | None, str]:
    """Validate that a string represents a valid priority level.

    Accepts full names (High, Medium, Low) or abbreviations (H, M, L).
    Case-insensitive. Empty string defaults to Medium.

    Args:
        value: The string to validate

    Returns:
        A tuple of (is_valid, priority_enum, error_message)
        - is_valid: True if the value is valid or empty
        - priority_enum: The Priority enum value if valid, None otherwise
        - error_message: Empty string if valid, error description otherwise

    Examples:
        >>> validate_priority("High")
        (True, Priority.HIGH, "")
        >>> validate_priority("m")
        (True, Priority.MEDIUM, "")
        >>> validate_priority("")
        (True, Priority.MEDIUM, "")
        >>> validate_priority("invalid")
        (False, None, "Invalid priority. Enter High/H, Medium/M, or Low/L (default: Medium)")
    """
    normalized = value.strip().lower()

    # Empty input defaults to Medium
    if not normalized:
        return True, Priority.MEDIUM, ""

    # Map inputs to Priority enum
    priority_map = {
        "high": Priority.HIGH,
        "h": Priority.HIGH,
        "medium": Priority.MEDIUM,
        "m": Priority.MEDIUM,
        "med": Priority.MEDIUM,
        "low": Priority.LOW,
        "l": Priority.LOW,
    }

    if normalized in priority_map:
        return True, priority_map[normalized], ""

    return (
        False,
        None,
        "Invalid priority. Enter High/H, Medium/M, or Low/L (default: Medium)",
    )
