
import click
from rich.console import Console
from utils.crud_handler import CRUDHandler

console = Console()
crud_handler = CRUDHandler('categories', 'project.json')

@click.group()
def categories():
    """Commands for managing categories."""
    pass

@categories.command()
@click.argument('name')
def create(name):
    """Create a new category."""
    crud_handler.create({'name': name, 'templates': []})
    console.print(f"Category '{name}' created.", style="bold green")

@categories.command()
def list():
    """List all categories."""
    categories = crud_handler.read()
    if categories:
        console.print("Categories:", style="bold blue")
        for category in categories:
            console.print(f"- {category['name']}", style="bold blue")
    else:
        console.print("No categories found.", style="bold red")

@categories.command()
@click.argument('name')
def show(name):
    """Show details of a category."""
    categories = crud_handler.read()
    category = next((cat for cat in categories if cat['name'] == name), None)
    if category:
        console.print(f"Category: {category['name']}", style="bold yellow")
        console.print(f"Templates: {category['templates']}", style="bold yellow")
    else:
        console.print(f"Category '{name}' not found.", style="bold red")

@categories.command()
@click.argument('name')
def delete(name):
    """Delete a category."""
    categories = crud_handler.read()
    category = next((cat for cat in categories if cat['name'] == name), None)
    if category:
        crud_handler.delete(category)
        console.print(f"Category '{name}' deleted.", style="bold red")
    else:
        console.print(f"Category '{name}' not found.", style="bold red")
