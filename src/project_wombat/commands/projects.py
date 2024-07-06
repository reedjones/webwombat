
import click
from rich.console import Console
from utils.crud_handler import CRUDHandler

console = Console()
crud_handler = CRUDHandler('projects', 'global_index.json')

@click.group()
def projects():
    """Commands for managing projects."""
    pass

@projects.command()
@click.argument('name')
def create(name):
    """Create a new project."""
    crud_handler.create({'name': name, 'location': '', 'details': {}})
    console.print(f"Project '{name}' created.", style="bold green")

@projects.command()
def list():
    """List all projects."""
    projects = crud_handler.read()
    if projects:
        console.print("Projects:", style="bold blue")
        for project in projects:
            console.print(f"- {project['name']} (Location: {project['location']})", style="bold blue")
    else:
        console.print("No projects found.", style="bold red")

@projects.command()
@click.argument('name')
def show(name):
    """Show details of a project."""
    projects = crud_handler.read()
    project = next((proj for proj in projects if proj['name'] == name), None)
    if project:
        console.print(f"Project: {project['name']}", style="bold yellow")
        console.print(f"Location: {project['location']}", style="bold yellow")
        console.print(f"Details: {project['details']}", style="bold yellow")
    else:
        console.print(f"Project '{name}' not found.", style="bold red")

@projects.command()
@click.argument('name')
def delete(name):
    """Delete a project."""
    projects = crud_handler.read()
    project = next((proj for proj in projects if proj['name'] == name), None)
    if project:
        crud_handler.delete(project)
        console.print(f"Project '{name}' deleted.", style="bold red")
    else:
        console.print(f"Project '{name}' not found.", style="bold red")
