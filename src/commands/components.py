# commands/components.py

import click
from rich.console import Console
from utils.crud_handler import CRUDHandler

console = Console()
crud_handler = CRUDHandler('components', 'project.json')

@click.group()
def components():
    """Commands for managing components."""
    pass

@components.command()
@click.argument('name')
def create(name):
    """Create a new component."""
    crud_handler.create({'name': name})
    console.print(f"Component '{name}' created.", style="bold green")

@components.command()
def list():
    """List all components."""
    components = crud_handler.read()
    if components:
        console.print("Components:", style="bold blue")
        for component in components:
            console.print(f"- {component['name']}", style="bold blue")
    else:
        console.print("No components found.", style="bold red")

@components.command()
@click.argument('name')
def delete(name):
    """Delete a component."""
    components = crud_handler.read()
    component = next((comp for comp in components if comp['name'] == name), None)
    if component:
        crud_handler.delete(component)
        console.print(f"Component '{name}' deleted.", style="bold red")
    else:
        console.print(f"Component '{name}' not found.", style="bold red")
