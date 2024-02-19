#!/usr/bin/python3
"""Defines the `State` class.

Sub-classes the `BaseModel` class.
"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel

class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )

    # Add the following foreign key relationship to BaseModel
    base_model_id = Column(String(60), ForeignKey('base_models.id'), nullable=False)
    base_model = relationship("BaseModel", back_populates="state")

    # Add the following line to establish the back-populated relationship
    BaseModel.state = relationship("State", back_populates="base_model")
