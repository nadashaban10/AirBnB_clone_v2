#!/usr/bin/python3
"""
__init__.py: Package initializer

Description:
    - Initializes the package with a DBStorage instance if HBNB_TYPE_STORAGE is 'db'
    - Otherwise, initializes the package with a FileStorage instance
    from the models.engine module.
    - It triggers a reload operation, loading existing data
    from file.json into memory.
"""

import os
from models.engine.file_storage import FileStorage

HBNB_TYPE_STORAGE = os.environ.get('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
