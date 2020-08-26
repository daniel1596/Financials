from pathlib import Path
from sqlite3 import connect

from py.Config import db_location, is_development


class FinancialsConnection:
    def __init__(self):
        self._connection = connect(database=db_location)

    def close(self):
        # Not sure if this will be needed; copied from bookcase
        self._connection.commit()
        self._connection.close()

    def execute(self, sql: str):
        # Trying this for debugging
        return self._connection.execute(sql)

    def execute_sql_file(self, sql_file_path: str, *, as_script=False):
        """
        Execute a SQL file with a given path.
        :return: Either nothing, if executed "as script", or the result set,
        """

        if not Path(sql_file_path).exists():
            raise IOError(f'This file path cannot be found: {sql_file_path}')
        
        with open(sql_file_path, 'r') as f:
            if as_script:
                self._connection.executescript(f.read())
                return

            return self._connection.execute(f.read())

    def initialize_tables(self):
        """
        Reset the db and
        """

        if is_development:
            for file_path in [
                'sql/ResetData.sql',
                'sql/CreateInsert_IncomeStatementLineItem.sql',
                'sql/CreateInsert_FinancialTransactionType.sql'
            ]:
                self.execute_sql_file(file_path, as_script=True)

        self.execute_sql_file('sql/CreateInsert_FinancialTransaction.sql', as_script=True)
        self.close()
