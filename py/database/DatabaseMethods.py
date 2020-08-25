from pathlib import Path
from shutil import copyfile

from py.database.FinancialsConnection import FinancialsConnection

_database_location = 'db/financials.sqlite'

"""This could be a wrapper class if needed around other FinancialsConnection methods."""

def backup_db_file():
    if not Path(_database_location).exists():
        pass # this would be an error

    backup_file_location = f'Backup of {_database_location}'
    copyfile(_database_location, backup_file_location)


def get_financial_transactions():
    connection = FinancialsConnection(_database_location)

    # I think this approach more or less works. The downside is that I would have to modify the SQL
    # in order to keep the Python fields in alignment.
    transactions_raw = connection.execute_sql_file('sql/Select_FinancialTransactions.sql')

    return [
        {'Amount': trans[0], 'Category': trans[1], 'Date': 'todo' } 
        for trans in transactions_raw
    ]


def initialize_database_first_run():
    if not Path(_database_location).exists():
        pass # create the database file at the command line maybe?

    connection = FinancialsConnection(_database_location)
    connection.initialize_tables()
    # connection.reset_data() # reset all data in the FinancialActivity table before Dad starts to use it
