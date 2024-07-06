
import click
from rich.console import Console
from utils.crud_handler import CRUDHandler
from utils.file_operations import read_json, write_json

console = Console()
crud_handler = CRUDHandler('categories', 'project.json')

@click.group()
def templates():
    """Commands for managing templates."""
    pass

@templates.command()
@click.argument('category')
@click.argument('name')
def create(category, name):
    """Create a new template."""
    categories = crud_handler.read()
    category_obj = next((cat for cat in categories if cat['name'] == category), None)
    if category_obj:
        category_obj['templates'].append(name)
        write_json('project.json', {'categories': categories})
        console.print(f"Template '{name}' created in category '{category}'.", style="bold green")
    else:
        console.print(f"Category '{category}' not found.", style="bold red")

@templates.command()
def list():
    """List all templates."""
    categories = crud_handler.read()
    if categories:
        console.print("Templates:", style="bold blue")
        for category in categories:
            console.print(f"Category: {category['name']}", style="bold blue")
            for template in category['templates']:
                console.print(f"  - {template}", style="bold blue")
    else:
        console.print("No templates found.", style="bold red")

@templates.command()
@click.argument('category')
@click.argument('name')
def show(category, name):
    """Show details of a template."""
    categories = crud_handler.read()
    category_obj = next((cat for cat in categories if cat['name'] == category), None)
    if category_obj:
        if name in category_obj['templates']:
            console.print(f"Template '{name}' in category '{category}'", style="bold yellow")
        else:
            console.print(f"Template '{name}' not found in category '{category}'", style="bold red")
    else:
        console.print(f"Category '{category}' not found.", style="bold red")

@templates.command()
@click.argument('category')
@click.argument('name')
def delete(category, name):
    """Delete a template."""
    categories = crud_handler.read()
    category_obj = next((cat for cat in categories if cat['name'] == category), None)
    if category_obj:
        category_obj['templates'] = [template for template in category_obj['templates'] if template != name]
        write_json('project.json', {'categories': categories})
        console.print(f"Template '{name}' deleted from category '{category}'.", style="bold red")
    else:
        console.print(f"Category '{category}' not found.", style="bold red")



# commands/templates.py

import click
import os
from rich.console import Console
from utils.crud_handler import CRUDHandler
from utils.file_operations import create_symbolic_link, remove_symbolic_link




@templates.command()
@click.argument('name')
@click.argument('category')
def create(name, category):
    """Create a new template."""
    templates = crud_handler.read()
    template_path = f"templates/{category}/{name}"
    if not os.path.exists(template_path):
        os.makedirs(template_path)
    crud_handler.create({'name': name, 'category': category})
    console.print(f"Template '{name}' created in category '{category}'.", style="bold green")

@templates.command()
def list():
    """List all templates."""
    templates = crud_handler.read()
    if templates:
        console.print("Templates:", style="bold blue")
        for template in templates:
            console.print(f"- {template['name']} (Category: {template['category']})", style="bold blue")
    else:
        console.print("No templates found.", style="bold red")

@templates.command()
@click.argument('name')
def delete(name):
    """Delete a template."""
    templates = crud_handler.read()
    template = next((temp for temp in templates if temp['name'] == name), None)
    if template:
        crud_handler.delete(template)
        template_path = f"templates/{template['category']}/{name}"
        if os.path.exists(template_path):
            os.rmdir(template_path)
        console.print(f"Template '{name}' deleted.", style="bold red")
    else:
        console.print(f"Template '{name}' not found.", style="bold red")

@templates.command()
@click.argument('template_name')
@click.argument('dependency_name')
def add_dependency(template_name, dependency_name):
    """Add a dependency to a template."""
    templates = crud_handler.read()
    template = next((temp for temp in templates if temp['name'] == template_name), None)
    dependency = next((temp for temp in templates if temp['name'] == dependency_name), None)
    if template and dependency:
        template_path = f"templates/{template['category']}/{template_name}/dependencies"
        if not os.path.exists(template_path):
            os.makedirs(template_path)
        dependency_path = f"../../{dependency['category']}/{dependency_name}"
        symbolic_link_path = f"{template_path}/{dependency_name}"
        create_symbolic_link(dependency_path, symbolic_link_path)
        console.print(f"Dependency '{dependency_name}' added to template '{template_name}'.", style="bold green")
    else:
        console.print(f"Template or dependency not found.", style="bold red")

@templates.command()
@click.argument('template_name')
@click.argument('dependency_name')
def remove_dependency(template_name, dependency_name):
    """Remove a dependency from a template."""
    templates = crud_handler.read()
    template = next((temp for temp in templates if temp['name'] == template_name), None)
    if template:
        template_path = f"templates/{template['category']}/{template_name}/dependencies/{dependency_name}"
        remove_symbolic_link(template_path)
        console.print(f"Dependency '{dependency_name}' removed from template '{template_name}'.", style="bold red")
    else:
        console.print(f"Template '{template_name}' not found.", style="bold red")
