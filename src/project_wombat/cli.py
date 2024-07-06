"""Console script for project_wombat."""
import project_wombat

import typer
from rich.console import Console

app = typer.Typer()
console = Console()
import click
from commands.categories import categories
from commands.projects import projects
from commands.templates import templates

@click.group()
def cli():
    pass

cli.add_command(categories)
cli.add_command(projects)
cli.add_command(templates)

if __name__ == '__main__':
    cli()

@app.command()
def main():
    """Console script for project_wombat."""
    console.print("Replace this message by putting your code into "
               "project_wombat.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
