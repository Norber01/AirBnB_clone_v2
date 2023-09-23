#!/usr/bin/python3
<<<<<<< HEAD
"""This is the base model class for the AirBnB"""
=======
"""This is the base model class for AirBnB"""
>>>>>>> 744e6d1d2dbae52e94b5e5fa3365be7ad8fc169e
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


<<<<<<< HEAD
=======

>>>>>>> 744e6d1d2dbae52e94b5e5fa3365be7ad8fc169e
class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """Instantiation of the base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at:the creation date
            updated_at:the updated date
=======
        """Instantiation of base model class
        Args:
            args: won't be useful
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creats date
            updated_at: updated date
>>>>>>> 744e6d1d2dbae52e94b5e5fa3365be7ad8fc169e
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
<<<<<<< HEAD
        """returns the string
        Return:
            returns the string of class name, id, and dictionary
=======
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
>>>>>>> 744e6d1d2dbae52e94b5e5fa3365be7ad8fc169e
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
<<<<<<< HEAD
        """return the string representaion
=======
        """return a string representaion
>>>>>>> 744e6d1d2dbae52e94b5e5fa3365be7ad8fc169e
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """creates dictionary of the class and returns
        Return:
            returns a dictionary of all the key values in __dict__
=======
        """creates dictionary for the class  and returns
        Return:
            returns a dictionary for all the key values in __dict__
>>>>>>> 744e6d1d2dbae52e94b5e5fa3365be7ad8fc169e
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """ delete object
        """
        models.storage.delete(self)
