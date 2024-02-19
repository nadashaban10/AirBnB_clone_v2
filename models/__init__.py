#!/usr/bin/python3
"""
__init__.py: Package initializer

Description:
    - Initializes the package with either a FileStorage or a DBStorage instance
      based on the value of HBNB_TYPE_STORAGE environment variable.
    - It triggers a reload operation, loading existing data
      from the storage into memory.
"""

import os
from models.engine import file_storage, db_storage

storage_type = os.environ.get('HBNB_TYPE_STORAGE', 'file')

if storage_type == 'db':
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()

storage.reload()
