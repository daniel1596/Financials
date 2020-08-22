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

def initialize_database_first_run():
    if not Path(_database_location).exists():
        pass # create the database file at the command line

    connection = FinancialsConnection(_database_location)
    connection.initialize_tables()
    connection.reset_data() # reset all data in the FinancialActivity table before Dad starts to use it