from pathlib import Path
from shutil import copyfile

from py.Config import db_location
from py.database.FinancialsConnection import FinancialsConnection


def backup_db_file():
    __ensure_db_file_exists()

    backup_file_location = f'Backup of {db_location}'
    copyfile(db_location, backup_file_location)


def get_financial_transactions():
    connection = FinancialsConnection()

    # New syntax is working great - thanks Stackoverflow.
    # The .description property allows me to match up Python dictionary keys with the SQL column mames.
    transactions_raw = connection.execute_sql_file('sql/Select_FinancialTransactions.sql')
    names = [description[0] for description in transactions_raw.description]

    return [{ names[i]: trans[i] for i in range(len(names))} for trans in transactions_raw]


def initialize_database_first_run():
    __create_db()

    connection = FinancialsConnection()
    connection.initialize_tables()


def __create_db():
    with open(db_location, 'w'):
        pass

    __ensure_db_file_exists()


def __ensure_db_file_exists():
    if not Path(db_location).exists():
        raise IOError("An error occurred when attempting to access the database file.")
