#!/usr/bin/python3
"""
Module containing the BaseModel class
"""
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import models

Base = declarative_base()


class BaseModel:
    """
    BaseModel class that defines common attributes/methods
    for other classes
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel

        Args:
            **kwargs: Arbitrary keyword arguments
        """
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.utcnow()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object

        Returns:
            str: String representation of the object
        """
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id,
                                    self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def delete(self):
        """Deletes the current instance from the storage
        """
        models.storage.delete(self)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance

        Returns:
            dict: Dictionary representation of the object
        """
        obj_dict = self.__dict__.copy()
        obj_dict.pop("_sa_instance_state", None)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
