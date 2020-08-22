from sqlite3 import connect


class FinancialsConnection:
    def __init__(self, db_location: str):
        self._connection = connect(database=db_location)
        # self.reset_data()

    def close(self):
        # Not sure if this will be needed; copied from bookcase
        self._connection.commit()
        self._connection.close()

    def initialize_tables(self):
        pass

    def reset_data(self):
        # This works! Not with a breakpoint... but exciting!
        # with open('sql/Select_FinancialTransactionType.sql', 'r') as f:
        #     for row in self._connection.execute(f.read()):
        #         print(row)

        # This works too! Tried this with some data in there.
        with open('sql/ResetData.sql', 'r') as f:
            self._connection.execute(f.read())

