#!/usr/bin/python3
"""review module contains the Review class implementation"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review inherits from BaseModel class and defines an review"""

    place_id = ""
    user_id = ""
    text = ""
