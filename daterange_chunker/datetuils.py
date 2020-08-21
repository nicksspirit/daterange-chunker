import datetime as dt
from typing import Generator, Tuple

Chunks = Generator[Tuple[dt.datetime, dt.datetime], None, None]


def calc_delta(startdate: dt.date, enddate: dt.date, no_of_ranges: int) -> dt.timedelta:
    """Find the delta between two dates based on a desired number of ranges"""
    date_diff = enddate - startdate
    steps = date_diff / no_of_ranges

    return steps


def chunk(startdate: dt.date, enddate: dt.date, delta=dt.timedelta(days=1)) -> Chunks:
    """
    Split a date range into a certain amount of equal sized chunks,
    evenly spaced by `delta`.
    """
    curr_date = to_datetime(startdate)
    end_date = to_datetime(enddate)

    while curr_date + delta <= end_date:
        to_date = curr_date + delta

        yield curr_date, to_date

        curr_date += delta


def is_delta_neg(startdate: dt.date, enddate: dt.date) -> bool:
    date_diff = enddate - startdate

    return date_diff < dt.timedelta(0)


def is_delta_gte_aday(delta: dt.timedelta) -> bool:
    return delta >= dt.timedelta(days=1)


def fmt_dates(dates, fmt="%Y-%m-%d %H:%M:%S") -> Tuple[str, ...]:
    return tuple(map(lambda d: d.strftime(fmt), dates))


def to_datetime(d: dt.date) -> dt.datetime:
    return dt.datetime.combine(d, dt.time.min)
