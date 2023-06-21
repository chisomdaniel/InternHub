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
    