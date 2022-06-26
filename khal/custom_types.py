import datetime as dt
from typing import Protocol, Tuple, TypedDict, Union

import pytz


class CalendarConfiguration(TypedDict):
    name: str
    path: str
    readonly: bool
    color: str
    priority: int
    ctype: str


class LocaleConfiguration(TypedDict):
    local_timezone: pytz.BaseTzInfo
    default_timezone: pytz.BaseTzInfo
    timeformat: str
    dateformat: str
    longdateformat: str
    datetimeformat: str
    longdatetimeformat: str
    weeknumbers: Union[str, bool]
    firstweekday: int
    unicode_symbols: bool


class SupportsRaw(Protocol):
    @property
    def uid(self) -> str:
        ...

    @property
    def raw(self) -> str:
        ...


# set this to TypeAlias once we support that python version (PEP613)
EventTuple = Tuple[
    str,
    str,
    Union[dt.date, dt.datetime],
    Union[dt.date, dt.datetime],
    str,
    str,
    str,
]