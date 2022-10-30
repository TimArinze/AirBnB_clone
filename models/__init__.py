#!/usr/bin/python3

"""
creating an instance of FileStorage for this application
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
