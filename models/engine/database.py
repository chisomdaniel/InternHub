#!/usr/bin/python3
''' Main database engine for our data'''
import os
from models.base import BaseModel
from models.internship import Internship
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


user = "internhub"
password = getenv('DB_PASS')  # get from evironment variable
host = "localhost"
database = "internhub_db"


class DB_engine:
    ''' Manage our database engine '''
    __engine = None
    __session = None

    def __init__(self):
        ''' start our DB engine '''
        string = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database)
        self.__engine = create_engine(string, pool_pre_ping=True)
    

    def new(self, obj):
        ''' Add obj to our database '''
        self.__session.add(obj)
    
    def all(self, cls=None):
        ''' Return a list (or dict) of our data '''
        if cls is None:
            objs = self.__session.query(Internship).all()
        else:
            classes = {"Internship": Internship}

            if cls not in classes.keys():
                if cls not in classes.values():
                    return
        
            if type(cls).__name__ == 'str':
                objs = self.__session.query(classes[cls])
            else:
                objs = self.__session.query(cls)

        new_dict = {}
        for obj in objs:
            new_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        ''' Save data to our relational db (mysql)'''
        self.__session.commit()
    
    def update(self):
        ''' Update data in database '''
    
    def delete(self, obj=None):
        ''' Delete a data from the database '''
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        ''' Reload our data instance from our database to python '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        ''' Close the current session '''
        self.__session.close()
