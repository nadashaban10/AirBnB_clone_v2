#!/usr/bin/python3
"""Defines the `City` class.

Sub-classes the `BaseModel` class.
"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city.

    Attributes:
        name (str): The name of the city.
        state_id (str): The state id.
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of City

        Args:
            **kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
