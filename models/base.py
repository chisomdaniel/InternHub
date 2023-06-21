#!/usr/bin/python3
'''The Base model for all our table models'''
from datetime import datetime
import uuid
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()

class BaseModel:
    ''' The base class for all our database models '''
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, **kwargs):
        if len(kwargs) > 3:
            self.id = kwargs.get('id') str(uuid.uuid4())
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def new(self):
        ''' Add new model instance to database'''
    
    def update(self):
        ''' Update or Model with new/updated info '''
    
    def save(self):
        ''' Save new model instance to database '''
    
    def delete(self):
        ''' Delete the current class instance '''
    
    def to_dict(self):
        ''' Return a dictionary representation of our model/data '''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
    
    def __str__(self):
        ''' A custom string for when our model is printed '''
        string = "{}:\n[{}]\n{}".format(self.__class__.__name__,
                                        self.id,
                                        self.to_dict)