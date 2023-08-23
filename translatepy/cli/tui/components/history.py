"""Deals with history requests response"""
import typing
from urllib.parse import urlparse

import requests
from textual.reactive import reactive
from textual.widgets import Button, Label

from nasse.tui.components import series


class HistoryResponse(Button):
    """A history response"""

    DEFAULT_CSS = """
    HistoryResponse {
        width: 100%;
        height: 3;
        color: $text;

        border: round white;
        padding: 0 1 0 1;
        height: auto;
        margin: 0 1 0 1;
        opacity: 1;
    }

    HistoryResponse:hover {
        opacity: 0.75;
    }

    Button:focus {}

    Button:hover {}

    .history-response-path {
        margin-bottom: 1;
    }

    .history-response-status {
        opacity: 0.75;
    }
    """

    response: reactive[typing.Union[requests.Response, "Error"]]

    def __init__(self, response: typing.Union[requests.Response, "Error"], **kwargs) -> None:
        super().__init__(**kwargs)
        self.response = response

    def compose(self):
        from nasse.tui.apps.http_app import Error

        url = urlparse(self.response.url)
        yield Label(f"[bold]{url.path}[/bold]", classes="history-response-path")

        if isinstance(self.response, Error):
            message = f"{self.response.method}・[yellow]{self.response.exception.__class__.__name__}[/yellow]"
        elif hasattr(self.response, "ok") and not self.response.ok:
            message = f"{self.response.request.method}・[red]{self.response.status_code}[/red] ({series.transform_time(self.response.elapsed.total_seconds() * 1000)})"
        elif hasattr(self.response, "request") and hasattr(self.response, "status_code") and hasattr(self.response, "elapsed"):
            message = f"{self.response.request.method}・{self.response.status_code} ({series.transform_time(self.response.elapsed.total_seconds() * 1000)})"
        else:
            message = "[yellow]ERROR[/yellow]"

        yield Label(message, classes="history-response-status")

    def render(self):
        return ""

    def _start_active_affect(self):
        return
