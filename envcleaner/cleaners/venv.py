import os
import shutil
import typer

from rich.console import Console
from rich.progress import track
from rich import print
from rich.table import Table


from envcleaner.cleaners.base import AbstractCleaner
from envcleaner.utils import check_path_exists, print_table

console = Console()

class VenvCleaner(AbstractCleaner):
    path: str

    def execute(self):
        if not check_path_exists(self.path, is_dir=True):
            print(f'[bold red]Past path is not from a folder.[/bold red]')
            raise typer.Exit()

        response = self.search_venv_in_folder()

        if not response:
            print(f'[bold red]No folders were found.[/bold red]')
            raise typer.Exit()

        print_table(response)

        typer.confirm(f'Do you really want to delete the above venv?', abort=True)
        self.delete_folders(response)

    def search_venv_in_folder(self):
        return [os.path.join(source, 'venv') for source, dirs, files in os.walk(self.path) if 'venv' in dirs]

    def delete_folders(self, folders: list):
        for value in track(folders, description="Deleting..."):
            self.delete_folder(value)

    @staticmethod
    def delete_folder(folder: str):
        try:
            shutil.rmtree(folder)
            print(f'[green]Folder removed: {folder}[/green]')
        except PermissionError:
            print(f'[bold red]Permission denied to remove: {folder} [/bold red]')
        except Exception as e:
            print(f'[bold red]{folder}: {e}[/bold red]')