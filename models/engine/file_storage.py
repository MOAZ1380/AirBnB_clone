import json
from models.base_model import BaseModel
import os




class FileStorage:
    
    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        return FileStorage.__objects
    
    
    
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    
    
    def save(self):
        obj_dict = {ke : val.to_dict() for ke, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as sa:
            json.dump(obj_dict, sa)
    
    
    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as re:
                obj_dict = json.load(re)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = globals()[class_name](**value)
                    FileStorage.__objects[key] = obj
            