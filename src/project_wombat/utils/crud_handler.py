import json
from utils.file_operations import read_json, write_json

class CRUDHandler:
    def __init__(self, entity_name, file_path):
        self.entity_name = entity_name
        self.file_path = file_path

    def create(self, item):
        data = read_json(self.file_path)
        if self.entity_name not in data:
            data[self.entity_name] = []
        data[self.entity_name].append(item)
        write_json(self.file_path, data)

    def read(self):
        data = read_json(self.file_path)
        return data.get(self.entity_name, [])

    def update(self, old_item, new_item):
        data = read_json(self.file_path)
        if self.entity_name in data:
            items = data[self.entity_name]
            if old_item in items:
                index = items.index(old_item)
                items[index] = new_item
                write_json(self.file_path, data)

    def delete(self, item):
        data = read_json(self.file_path)
        if self.entity_name in data:
            data[self.entity_name] = [i for i in data[self.entity_name] if i != item]
            write_json(self.file_path, data)