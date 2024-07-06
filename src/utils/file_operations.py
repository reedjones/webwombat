
import json
import os

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
        


def create_symbolic_link(source, target):
    try:
        os.symlink(source, target)
    except OSError as e:
        print(f"Failed to create symbolic link: {e}")

def remove_symbolic_link(link_path):
    try:
        os.remove(link_path)
    except OSError as e:
        print(f"Failed to remove symbolic link: {e}")