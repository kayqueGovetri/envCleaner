import os

from rich.console import Console
from rich.table import Table


def check_path_exists(path: str, is_dir = True):
    if not is_dir:
        return os.path.exists(path)
    return os.path.isdir(path)


def print_table(items: list):
    console = Console()
    table = Table("Folder")
    for item in items:
        table.add_row(item)
    console.print(table)