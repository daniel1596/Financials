from py.database.DatabaseHelper import DatabaseHelper
from py.database.FinancialsConnection import FinancialsConnection
from py.models.Quarter import Quarter


class FinancialDatabaseHelper(DatabaseHelper):
    """
    Subclass specifically for this application.
    I feel like this could be a singleton (db = FinancialDatabaseHelper()), but I'm not sure if that would be best practice.
    """
    def __init__(self):
        self._connection = FinancialsConnection()


    def get_financial_transactions(self, year: int=None, quarter: Quarter=None, include_income_statement_line_item: bool=False):
        # Building out the raw SQL, in this case, is actually going to be preferable for performance.
        fields_to_select = "ft.Amount, ft.DateYear, ft.DateMonth, ft.DateDay, ftt.Category"
        inner_joins = "INNER JOIN FinancialTransactionType ftt ON ftt.FinancialTransactionTypeID=ft.FinancialTransactionTypeID"

        if include_income_statement_line_item:
            inner_joins += " INNER JOIN IncomeStatementLineItem isli ON isli.IncomeStatementLineItemID=ftt.IncomeStatementLineItemID"
            fields_to_select += ", isli.Description"

        if (not year) and (not quarter):
            where = "1=1"
        elif not quarter:
            where = f"ft.DateYear = {year}"
        else:
            where = f"ft.DateYear = {year}" \
                    f" AND ft.DateMonth >= {quarter.month_first}" \
                    f" AND ft.DateMonth <= {quarter.month_last}"

        sql = f"SELECT {fields_to_select} " \
              f"FROM FinancialTransaction ft " \
              f" {inner_joins} " \
              f"WHERE {where}"

        transactions_raw = self._connection.execute(sql)

        # New syntax is working great - thanks Stackoverflow.
        # The .description property allows me to match up Python dictionary keys with the SQL column mames.
        names = [description[0] for description in transactions_raw.description]

        return [{ names[i]: trans[i] for i in range(len(names))} for trans in transactions_raw]


    def get_income_statement_line_items(self, *, include_calculated_line_items=True):
        connection = FinancialsConnection()

        query = "SELECT Description FROM IncomeStatementLineItem"
        if not include_calculated_line_items:
            query += " WHERE IsCalculatedLineItem = 0"

        return [line_items[0] for line_items in connection.execute(query)]


    def initialize_database_first_run(self):
        """
        Create the database and tables for the first time.
        If Daniel is running this method repeatedly, note that no "DELETE FROM <tablename>" script will be necessary,
        as self._create_db() opens the db file in "write" mode, thus wiping it out.
        """
        self._create_db()
        self._connection.create_tables()


