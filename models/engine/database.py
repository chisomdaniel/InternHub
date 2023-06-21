#!/usr/bin/python3
''' Main database engine for our data'''
import os
from models.Base import BaseModel
from models.internship import Internship
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


user =
password =
host =
database =


class DB_engine:
    ''' Manage our database engine '''
    __engine = None
    __session = None

    def __init__(self):
        ''' start our DB engine '''
        string = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database)
        self.__engine = create_engine(string, pool_pre_ping=True)
    

    def create(self):
        ''' Create our database '''
    
    def all(self):
        ''' Return a list (or dict) of our data '''
    
    def save(self):
        ''' Save data to our relational db (mysql)'''
    
    def update(self):
        ''' Update data in database '''
    
    def delete(self):
        ''' Delete a data from the database '''
    
    def reload(self):
        ''' Reload our data instance from our database to python '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        ''' Close the current session '''
        self.__session.close()
