"""Displays a series nicely"""

import statistics
import typing

from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Label, Sparkline

from nasse.tui.widget import Widget
from nasse.localization import EnglishLocalization, Localization


def transform_time(value: typing.Union[int, float]):
    """
    Transforms the milliseconds to a human readable but also width fixed string

    Here are the different transformations :
    5 slots available: xxxxx
    | Unit             | First | Second| Third | Fourth|
    | ---------------- | ----- | ----- | ----- | ----- |
    | 1 d = 24 h       | 9d23h | 99  d | 999 d | 9999d |
    | 1 h = 3600 s     | 9h59m | 99h59 |       |       |
    | 1 s = 1000 ms    | 9.99s | 99.9s | 999 s | 9999s |
    | 1 ms             | 9.9ms | 99 ms | 999ms |       |
    """
    if value >= 360_000_000:  # 100 hours
        # days format
        value /= 86_400_000  # 1 day
        days = int(value)
        value -= days
        hours = int(value * 24)  # 1 hour
        if days >= 10:
            return f"{days}{' ' * (4 - len(str(days)))}d"
        else:
            return f"{days}d{str(hours).zfill(2)}h"
    elif value >= 10_000_000:  # 10 000 seconds
        # hours format
        value /= 3_600_000
        hours = int(value)
        value -= hours
        minutes = int(value * 60)  # 1 minute
        if hours >= 10:
            return f"{hours}h{str(minutes).zfill(2)}"
        else:
            return f"{hours}h{str(minutes).zfill(2)}m"
    elif value >= 1000:  # 1 000 milliseconds
        # seconds format
        seconds = value / 1000
        if seconds >= 1000:
            return f"{int(seconds)}s"
        elif seconds >= 100:
            return f"{int(seconds)} s"
        else:
            digits = 1 if seconds >= 10 else 2
            seconds = str(round(seconds, digits))
            while len(seconds) < 4:
                seconds += "0"
            return f"{seconds}s"
    else:
        # milliseconds format
        if value >= 100:
            return f"{int(value)}ms"
        elif value >= 10:
            return f"{int(value)} ms"
        else:
            value = str(float(round(value, 1)))
            while len(value) < 3:
                value += " "
            return f"{value}ms"


class TimeSeries(Widget):
    """A time series widget"""
    DEFAULT_CSS = """
    TimeSeries {
        height: auto;
        width: 34;
    }
    TimeSeries > Label {
        margin: 0 1 0 1;
        align-horizontal: center;
    }
    """
    series: reactive[typing.List[int]] = reactive(list)

    def __init__(self, series: typing.Optional[typing.List[int]] = None, localization: typing.Type[Localization] = EnglishLocalization, **kwargs) -> None:
        super().__init__(**kwargs)
        self.series = series or []
        self.localization = localization

    @property
    def statistics(self):
        """Returns a statistics banner for the series"""
        min_ping = min(self.series) if self.series else 0
        max_ping = max(self.series) if self.series else 0
        avg_ping = statistics.mean(self.series) if self.series else 0

        return f"{self.localization.min} {transform_time(min_ping)} / {self.localization.average} {transform_time(avg_ping)} / {self.localization.max} {transform_time(max_ping)}"

    def compose(self) -> ComposeResult:
        yield Label(self.statistics)
        yield Sparkline(
            self.series,
            summary_function=statistics.mean
        )

    def watch_series(self, series: typing.List[int]):
        """When the `series` attribute is set"""
        try:
            self.query_one(Label).update(self.statistics)
            self.query_one(Sparkline).data = series
        except Exception as err:
            print("WARNING: Couldn't update view;", err)
