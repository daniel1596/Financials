from abc import abstractmethod
from pathlib import Path
from shutil import copyfile

from py.Config import db_location


class DatabaseHelper:
    """Base class for handling db operations."""

    def backup_db_file(self):
        self._ensure_db_file_exists()

        backup_file_location = f'Backup of {db_location}'
        copyfile(db_location, backup_file_location)


    def _create_db(self):
        with open(db_location, 'w'):
            pass

        self._ensure_db_file_exists()


    def _ensure_db_file_exists(self):
        if not Path(db_location).exists():
            raise IOError("An error occurred when attempting to access the database file.")