#!/usr/bin/python3
"""   Defines all common attributes/methods for other classes """

import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):

        """Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue

                if key == 'created_at' or key == 'updated_at':

                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):

        """Returns a readable string representation
        of BaseModel instances"""

        return f"[{self.__class__.__name__}] ({self.id}){self.__dict__}"

    def save(self):

        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary that contains all
        keys/values of the instance"""
        my_dic = self.__dict__.copy()
        my_dic['created_at'] = self.created_at.isoformat()
        my_dic['updated_at'] = self.updated_at.isoformat()
        my_dic['__class__'] = self.__class__.__name__

        return my_dic
