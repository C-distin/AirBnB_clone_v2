#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os

STORAGE_TYPE = os.getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    if STORAGE_TYPE == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place',
            secondary='place_amenity',
            back_populates='amenities'
        )
    else:
        name = ""
