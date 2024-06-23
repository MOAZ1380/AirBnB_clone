import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        
        if kwargs:
            for key , value in kwargs.items():
                if key == __class__:
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                self.key = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}){self.__dict__}"
    
    
    
    def save(self):
        self.updated_at = datetime.now()
    
    
    
    
    def to_dict(self):
        my_dic = self.__dict__.copy()
        my_dic['created_at'] = self.created_at.isoformat()
        my_dic['updated_at'] = self.created_at.isoformat()
        my_dic['__class__'] = self.__class__.__name__
        
        return my_dic
    