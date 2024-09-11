"""
Validator Utilities

This module provides a collection of utility functions for validating various types of data.
These functions are designed to be reusable and can be easily integrated into different projects
to ensure data integrity and correctness.
"""


from datetime import datetime
import re


def is_valid_date(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Validates if the provided date string matches the specified format.

    Args:
        date_str (str): The date string to check.
        date_format (str, optional): The format to validate against (default is '%Y-%m-%d').

    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    if date_str is None or date_str.strip() == "":
        return False
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        # Return False if date parsing fails
        return False


def validate_number(input_value, lower_bound=None, upper_bound=None):
    """
    Checks if the input value is a valid number and optionally verifies
    it against minimum and maximum limits.

    Args:
        input_value: A string or number to check.
        lower_bound: Optional minimum permissible value.
        upper_bound: Optional maximum permissible value.

    Returns:
        bool: True if the input value is a valid number and meets the bounds,
        False otherwise.
    """
    if input_value is None:
        return True

    try:
        num = float(input_value)  # Try to convert the input to a number
        if lower_bound is not None and num < lower_bound:
            return False
        if upper_bound is not None and num > upper_bound:
            return False
        return True
    except ValueError:
        return False  # Input is not a valid number


def validate_integer(input_value, lower_bound=None, upper_bound=None):
    """
    Checks if the input value is an integer
    (either as an actual integer or a string representation).

    Args:
        input_value: An integer or a string representing an integer.
        lower_bound: Optional minimum permissible value.
        upper_bound: Optional maximum permissible value.

    Returns:
        bool: True if the input value is a valid integer, False otherwise.
    """
    if input_value is None:
        return True

    try:
        num = int(input_value)  # Try to convert the input to an integer
        if lower_bound is not None and num < lower_bound:
            return False
        if upper_bound is not None and num > upper_bound:
            return False
        # Ensure the converted integer matches the original input
        return str(num) == str(input_value)
    except ValueError:
        return False  # Input is not a valid integer


def validate_email(email_address):
    """
    Validates whether the provided email address is in a proper format.

    Args:
        email_address (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.

    Examples:
        >>> validate_email("example@example.com")
        True
        >>> validate_email("invalid-email")
        False
        >>> validate_email("another.example@domain.co")
        True
        >>> validate_email("bad..email@domain.com")
        False
    """
    email_pattern = r"^(?!.*\.\.)(?!.*\.$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not isinstance(email_address, str):
        return False
    if re.match(email_pattern, email_address):
        return True
    return False
