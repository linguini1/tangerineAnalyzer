# Utilities to get dates
__author__ = "Matteo Golin"

# Imports
import datetime as dt
import dateutil.relativedelta as rd
import functools
from customtypes import DateRange, DateRangeString
from typing import Callable


# Constants
DATE_FORMAT = "%#m/%#d/%Y"


# Functions
def range_to_string(date_maker: Callable[[int], DateRange]) -> Callable[[], DateRangeString]:

    """Decorator to turn date ranges into a tuple of strings in the format m/d/yyyy."""

    @functools.wraps(date_maker)
    def wrapper(*args, **kwargs) -> list[str]:
        dates = date_maker(*args, **kwargs)
        return [date.strftime(DATE_FORMAT) for date in dates]

    return wrapper


@range_to_string
def past_days(days: int = 1) -> DateRange:

    """Returns a date range for the past number of weeks passed."""

    today = dt.date.today()
    past_day = today - dt.timedelta(days=days)

    return [today - dt.timedelta(days=_) for _ in range((today - past_day).days + 1)]


@range_to_string
def past_weeks(weeks: int = 1) -> DateRange:

    """Returns a date range for the past number of weeks passed."""

    today = dt.date.today()
    past_day = today - dt.timedelta(days=7 * weeks)

    return [today - dt.timedelta(days=_) for _ in range((today - past_day).days + 1)]


@range_to_string
def past_months(months: int = 1) -> DateRange:

    """Returns a date range for the past number of months passed."""

    today = dt.date.today()
    past_day = today - rd.relativedelta(months=months)

    return [today - dt.timedelta(days=_) for _ in range((today - past_day).days + 1)]


@range_to_string
def past_year() -> DateRange:

    """Returns a date range for the past year."""

    today = dt.date.today()
    past_day = today - rd.relativedelta(years=1)

    return [today - dt.timedelta(days=_) for _ in range((today - past_day).days + 1)]

