from pathlib import Path
from sqlite3 import connect

from py.helpers.ConfigHelper import config
from py.helpers.FileHelper import FileHelper


class DatabaseHandler:
    """Base class for handling db operations."""
    def __init__(self):
        self._connection = connect(database=config.db_location)

    @classmethod
    def backup_db_file(cls):
        FileHelper.ensure_file_exists(config.db_path)

        backup_file_path = f'Backup of {config.db_location}'
        FileHelper.copy_file(config.db_location, backup_file_path)

    def close_connection(self):
        # Not sure if this will be needed; copied from bookcase
        self._connection.commit()
        self._connection.close()

    def execute(self, sql: str, *, as_script: bool=False):
        if as_script:
            self._connection.executescript(sql)
            return  # there is no value to return; .executescript() does not return anything

        return self._connection.execute(sql)

    def execute_sql_file(self, sql_file_path: str, *, as_script: bool=False):
        """
        Execute a SQL file with a given path.
        :return: Either nothing, if executed "as script", or the result set
        """

        if not Path(sql_file_path).exists():
            raise IOError(f'This file path cannot be found: {sql_file_path}')

        with open(sql_file_path, 'r') as f:
            self.execute(f.read(), as_script=as_script)