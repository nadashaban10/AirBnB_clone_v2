#!/usr/bin/python3
"""Module defining the Review class."""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """Review class representing a review in the database.

    Attributes:
        __tablename__ (str): Name of the MySQL table for Review objects.
        text (sqlalchemy String): Description of the review.
        place_id (sqlalchemy String): ID of the place being reviewed.
        user_id (sqlalchemy String): ID of the user who wrote the review.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
