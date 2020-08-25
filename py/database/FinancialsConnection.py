from pathlib import Path
from sqlite3 import connect


class FinancialsConnection:
    def __init__(self, db_location: str):
        self._connection = connect(database=db_location)
        # self.reset_data()

    def close(self):
        # Not sure if this will be needed; copied from bookcase
        self._connection.commit()
        self._connection.close()

    def execute(self, sql: str):
        # Trying this for debugging
        return self._connection.execute(sql)

    def execute_sql_file(self, sql_file_path: str, *, as_script=False):  # returns a row
        if not Path(sql_file_path).exists():
            print('this path does not exist for ' + sql_file_path)
        
        with open(sql_file_path, 'r') as f:
            if as_script:
                return self._connection.executescript(f.read())
            else:
                return self._connection.execute(f.read())

    def initialize_tables(self):
        for file_path in [
            'sql/CreateInsert_IncomeStatementLineItem.sql',
            'sql/CreateInsert_FinancialTransactionType.sql',
            'sql/Create_FinancialTransaction.sql'
        ]:
            self.execute_sql_file(file_path, as_script=True)
        
        self.close()

    def reset_data(self):
        self.execute_sql_file('sql/ResetData.sql', as_script=True)
        self.close()


