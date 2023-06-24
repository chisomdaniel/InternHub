#!/usr/bin/python3
''' Model for our internships posting info '''
from models.base import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime


class Internship(BaseModel, Base):
    ''' Internship database model '''
    __tablename__ = "internships"

    title = Column(String(50), nullable=False)
    company = Column(String(50), nullable=False)
    company_website = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)   # company email
    phone_number = Column(Integer, nullable=True)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    position_type = Column(String(50), nullable=False, default="Internship")
    description = Column(String(1000), nullable=False)
    responsibility = Column(String(1000), nullable=False)
    requirement = Column(String(1000), nullable=False)
    skill = Column(String(1000), nullable=False)
    benefit = Column(String(1000), nullable=True)
    apply = Column(String(1000), nullable=False)  # How to apply
    expire = Column(String(50), nullable=True)  # when does application close "in string format"
    note = Column(String(1000), nullable=True)  # include any additional note
    closing = Column(String(1000), nullable=True)   # add an optional closing statement

    def __init__(self, *arg, **kwargs):
        ''' Instantiate our Internship class,

        First create the the default attribute from the `BaseModel class`,
        then set the object attribute from the kwards argument passed.

        `**kwarg` must be passed to the class when creating it
        '''
        super().__init__()

        ignore = ['id', 'updated_at', 'created_at', '__class__']
        if len(kwargs.keys()) >= 12:
            for key, value in kwargs.items():
                if key in ignore:
                    continue
                setattr(self, key, value)
            self.save()
        else:
            print("[Error] Incomplete parameters to create model.")
    