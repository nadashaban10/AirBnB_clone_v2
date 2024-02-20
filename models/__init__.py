#!/usr/bin/python3
"""
__init__.py: Package initializer

Description:
    - Initializes the package with either a FileStorage or DBStorage instance
      based on the value of the environment variable HBNB_TYPE_STORAGE.
    - It triggers a reload operation, loading existing data
      from the database or file.json into memory.
"""

import os
from models.engine import file_storage, db_storage

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()

storage.reload()
