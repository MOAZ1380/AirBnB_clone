"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place

import os




class FileStorage:
    """The file storage engine class, that is;
    A class that serialize and deserialize instances to a JSON file
    """
    
    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects
    
    
    
    
    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {ke : val.to_dict() for ke, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as sa:
            json.dump(obj_dict, sa, indent=4)
    
    
    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        
        class_d = {
            "BaseModel" : BaseModel,
            "User" : User,
            "Place" : Place,
            "State" : State,
            "Review" : Review,
            "Amenity" : Amenity,
            "City" : City
        }
        
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as re:
                obj_dict = json.load(re)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = class_d[class_name](**value)
                    FileStorage.__objects[key] = obj
            