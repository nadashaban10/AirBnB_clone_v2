#!/usr/bin/python3
"""Defines the `City` class.

Sub-classes the `BaseModel` class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")