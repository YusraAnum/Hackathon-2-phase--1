"""Input validation utilities for the CLI."""


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
