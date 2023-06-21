#!/usr/bin/python3
'''The Base model for all our table models'''
import datetime
import uuid
import os
import sqlalchemy


class BaseModel:

    def __init__(self, **args):
        if args:
        
        id = ""
        created_at = ""
        updated_at = ""
    
    def new(self):
        ''' Add new model instance to database'''
    
    def update(self):
        ''' Update or Model with new/updated info '''
    
    def save(self):
        ''' Save new model instance to database '''
    
    def to_dict(self):
        ''' Output a dictionary representation of our model/data '''
    
    def __str__(self):
        ''' A custom string for when our model is printed '''