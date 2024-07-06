import os
import json

# Define the directory structure and component template
app_structure = {
    "src": {
        "components": {
            "Authentication": {
                "pages": ["LoginPage.js"],
                "sections": [],
                "molecules": [],
                "atoms": ["TextInput.js", "Button.js"]
            },
            "ComponentExtraction": {
                "pages": ["ComponentExtractionPage.js"],
                "sections": ["ComponentInputSection.js", "ComponentActionsSection.js"],
                "molecules": ["ComponentForm.js"],
                "atoms": ["TextInput.js", "Button.js"]
            },
            "ComponentCollection": {
                "pages": ["ComponentCollectionPage.js"],
                "sections": ["TagFilterSection.js", "ComponentListSection.js", "ExportSection.js"],
                "molecules": ["EditComponentModal.js"],
                "atoms": ["Button.js", "Dropdown.js"]
            },
            "SyncError": {
                "pages": ["SyncErrorPage.js"],
                "sections": ["ErrorMessageSection.js", "RetrySection.js"],
                "molecules": [],
                "atoms": ["Button.js"]
            },
            "Spinner": {
                "pages": [],
                "sections": [],
                "molecules": [],
                "atoms": ["Spinner.js"]
            },
            "Highlighter": {
                "pages": [],
                "sections": [],
                "molecules": [],
                "atoms": ["HighlighterToggle.js"]
            },
            "Toolbar": {
                "pages": [],
                "sections": [],
                "molecules": [],
                "atoms": ["ToolbarButton.js"]
            }
        }
    }
}

# Component template for React functional components
component_template = '''\
import React from 'react';

const {} = () => {
  return (
    <div>
      {/* Replace with component content */}
      <h2>{}</h2>
    </div>
  );
};

export default {};
'''

# Create directories and files based on app_structure
def create_app_structure(structure):
    for directory, contents in structure.items():
        os.makedirs(directory, exist_ok=True)
        for component, categories in contents.items():
            component_path = os.path.join(directory, component)
            os.makedirs(component_path, exist_ok=True)
            for category, files in categories.items():
                category_path = os.path.join(component_path, category)
                os.makedirs(category_path, exist_ok=True)
                for file in files:
                    file_path = os.path.join(category_path, file)
                    with open(file_path, 'w') as f:
                        # Use the template to write content to the file
                        component_name = file.replace('.js', '')
                        f.write(component_template.format(component_name, component_name, component_name))

# JSON data for any additional configuration or metadata
data = {
    "app_name": "WebElementsApp",
    "author": "Your Name",
    "description": "A React application for managing web elements",
    "version": "1.0.0"
}

# Write JSON data to a file
def write_json(data, filename='config.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Main execution
if __name__ == "__main__":
    create_app_structure(app_structure)
    write_json(data)
    print("App structure and files created successfully!")
