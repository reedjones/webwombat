==============
Project Wombat
==============



.. image:: /wombat.jpg
        :target: https://github.com/reedjones/webwombat




WebWombat
=========

WebWombat is a CLI tool for managing web projects, including templates, components, and projects with support for atomic design principles and template hierarchies. It utilizes symbolic links for managing dependencies, ensuring efficient and non-redundant template usage.

Usage
-----

Components Commands:

- ``webwombat components create <name>``: Create a new component.
- ``webwombat components list``: List all components.
- ``webwombat components delete <name>``: Delete a component.

Templates Commands:

- ``webwombat templates create <name> <category>``: Create a new template in a specific category.
- ``webwombat templates list``: List all templates.
- ``webwombat templates delete <name>``: Delete a template.
- ``webwombat templates add_dependency <template_name> <dependency_name>``: Add a dependency to a template.
- ``webwombat templates remove_dependency <template_name> <dependency_name>``: Remove a dependency from a template.

Projects Commands:

- ``webwombat projects create <name>``: Create a new project.
- ``webwombat projects list``: List all projects.
- ``webwombat projects delete <name>``: Delete a project.

* Free software: MIT license
* Documentation: https://project-wombat.readthedocs.io.

Features
--------

* Manage web project components and templates using atomic design principles.
* Create, list, and delete components.
* Create, list, and delete templates in specific categories.
* Manage dependencies between templates using symbolic links.
* Create, list, and delete web projects.
* Maintain a global index of all projects and their locations.

Credits
-------
* Author: reedjones
* License: MIT