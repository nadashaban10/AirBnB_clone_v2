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

    base_model_id = Column(String(60), ForeignKey('base_models.id'), nullable=False)
    base_model = relationship("BaseModel", back_populates="state")

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of State

        Args:
            **kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)

    BaseModel.state = relationship("State", back_populates="base_model")
