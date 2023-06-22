#!/usr/bin/python3
''' Model for our internships posting info '''
from models import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime


class Internship(BaseModel, Base):
    ''' Internship database model '''
    __tablename__ = "internships"

    title = Column(String(128), nullable=False)
    company = ""
    company_website = ""
    email = ""
    phone_number = ""
    city = ""
    state = ""
    position_type = ""
    description = ""
    responsibility = ""
    requirement = ""
    skill = ""
    benefit = ""
    apply = ""
    expire = ""
    note = ""  # include any additional note
    closing = ""   # add an optional closing statement

    def __init__(self, **kwargs):
        ''' Instantiate our Internship class,

        First create the the default attribute from the `BaseModel class`,
        then set the object attribute from the kwards argument passed.

        `**kwarg` must be passed to the class when creating it
        '''
        super().__init__()

        if **kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
            self.save()
        else:
            print("[Error] Incomplete parameters to create model.")
    