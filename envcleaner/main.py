import typer

from envcleaner.cleaners.venv import VenvCleaner

app = typer.Typer(help="CLI to help clean up unused venv in folders.")


@app.command()
def cleaner(path: str):
    """
    Pass the path you want to delete the venv
    """
    path = VenvCleaner(path=path)
    path.execute()
