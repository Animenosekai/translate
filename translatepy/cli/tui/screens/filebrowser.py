"""A file explorer"""
import pathlib
import typing

from textual import events
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual.widgets import DirectoryTree, Label, Tree
from textual.widgets._directory_tree import DirEntry
from nasse.localization import Localization, EnglishLocalization


class FilteredDirectoryTree(DirectoryTree):
    """A filtered directory tree"""
    filter: reactive[typing.Optional[str]] = reactive(None)

    def filter_paths(self, paths: typing.Iterable[pathlib.Path]) -> typing.Iterable[pathlib.Path]:
        if not self.filter:
            return paths
        return [path for path in paths if str(path.resolve()).casefold().startswith(self.filter) or path.name.casefold().startswith(self.filter)]

    def watch_filter(self, filter: typing.Optional[str]):
        """When the filter is changed"""
        self.reload()


class FileBrowser(ModalScreen[typing.Optional[pathlib.Path]]):
    """A file browser"""
    selected: reactive[pathlib.Path] = reactive(pathlib.Path)

    DEFAULT_CSS = """
    FileBrowser {
        height: 80vh;
        width: 80vw;
    }
    #filter-label {
        opacity: 1;
        height: auto;
        background: $panel-darken-1;
        width: 100vw;
        padding: 0 1;
    }

    #filter-label.hidden {
        opacity: 0;
    }
    """
    def __init__(self, localization: typing.Type[Localization] = EnglishLocalization, **kwargs) -> None:
        super().__init__(**kwargs)
        self.localization = localization

    def compose(self):
        yield Label(str(pathlib.Path().resolve()), id="file-browser-title")
        yield FilteredDirectoryTree(pathlib.Path())
        yield Label("", id="filter-label")

    def go_back(self) -> None:
        """When the user wants to go back"""
        tree = self.query_one(FilteredDirectoryTree)
        tree.path = pathlib.Path(tree.path).resolve().parent

    def go_forward(self) -> None:
        """When the user wants to go back"""
        tree = self.query_one(FilteredDirectoryTree)
        path = self.selected.resolve()
        if path.is_dir():
            tree.path = path

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted[DirEntry]):
        """When a node is highlited"""
        if not event.node.data:
            return
        path = event.node.data.path.resolve()
        self.selected = path

    def watch_selected(self, selected: pathlib.Path):
        """When the selection changed"""
        parent, sep, filename = str(selected).rpartition("/")

        if not filename:
            parent, sep, filename = str(selected).rpartition("\\")

        self.query_one("#file-browser-title", Label).update(f"[grey]{parent}{sep}[/grey][bold]{filename}[/bold]")

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected):
        """When a file is selected"""
        if self.selected.is_file():
            self.dismiss(self.selected)

    def on_key(self, event: events.Key) -> None:
        """When a key is pressed on the keyboard"""
        directory_tree = self.query_one(FilteredDirectoryTree)
        if event.key == "escape":
            if not directory_tree.filter:
                self.dismiss(None)
            else:
                directory_tree.filter = None
        elif event.key == "delete" or event.key == "backspace":
            if directory_tree.filter:
                directory_tree.filter = directory_tree.filter[:-1]
        elif event.key == "left":
            self.go_back()
        elif event.key == "right":
            self.go_forward()
        elif event.is_printable and event.character:
            if directory_tree.filter:
                directory_tree.filter += event.character.casefold()
            else:
                directory_tree.filter = event.character.casefold()

        label = self.query_one("#filter-label", Label)
        if directory_tree.filter:
            label.update(f"[grey]{self.localization.filter}:[/grey] [bold]{directory_tree.filter}[/bold]")
            label.remove_class("hidden")
        else:
            label.add_class("hidden")
