from py.helpers.ConfigHelper import config
from py.helpers.FileHelper import FileHelper


class DatabaseHelper:
    """Base class for handling db operations."""

    @classmethod
    def backup_db_file(cls):
        FileHelper.ensure_file_exists(config.db_location)

        backup_file_path = f'Backup of {config.db_location}'
        FileHelper.copy_file(config.db_location, backup_file_path)


    @classmethod
    def _create_db(cls):
        FileHelper.create_file(config.db_location)
