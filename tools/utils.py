from datetime import date, datetime, timedelta


def add_days(date_input, days: int, date_format='%Y-%m-%d'):
  """
    Adds a specified number of days to a given date.

    Parameters:
    date_input (str, datetime.date, datetime.datetime): The initial date.
    days (int): The number of days to add.

    Returns:
    str: The new date as a string in the format 'yyyy-mm-dd'.
    """
  
    # Check the type of date_input and convert to datetime if necessary
    if isinstance(date_input, str):
        date_obj = datetime.strptime(date_input, date_format)
    elif isinstance(date_input, date):
        date_obj = datetime.combine(date_input, datetime.min.time())
    elif isinstance(date_input, datetime):
        date_obj = date_input
    else:
        raise TypeError("date_input must be a string, "
                        "datetime.date, or datetime.datetime")

    # Add the specified number of days
    new_date = date_obj + timedelta(days=days)

    return new_date.strftime(date_format)
