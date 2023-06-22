#!/usr/bin/python3
''' Model for our internships posting info '''
from models.base import Base, BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime


class Internship(BaseModel, Base):
    ''' Internship database model '''
    __tablename__ = "internships"

    title = Column(String(128), nullable=False)
    company = Column(String(128), nullable=False)
    company_website = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)   # company email
    phone_number = Column(Integer(20), nullable=True)
    city = Column(String(128), nullable=False)
    state = Column(String(128), nullable=False)
    position_type = Column(String(128), nullable=False, default="Internship")
    description = Column(String(2000), nullable=False)
    responsibility = Column(String(2000), nullable=False)
    requirement = Column(String(2000), nullable=False)
    skill = Column(String(2000), nullable=False)
    benefit = Column(String(2000), nullable=True)
    apply = Column(String(2000), nullable=False)  # How to apply
    expire = Column(String(128), nullable=False)  # when does application close "in string format"
    note = Column(String(2000), nullable=False)  # include any additional note
    closing = Column(String(2000), nullable=False)   # add an optional closing statement

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
    