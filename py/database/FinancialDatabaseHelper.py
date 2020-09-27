from py.database.DatabaseHandler import DatabaseHandler
from py.models.Quarter import Quarter


class FinancialDatabaseHandler(DatabaseHandler):
    """
    Subclass specifically for this application.
    I feel like this could be a singleton (db = FinancialDatabaseHelper()), but I'm not sure if that would be best practice.
    """

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
        # The .description property allows me to match up Python dictionary keys with the SQL column names.
        names = [description[0] for description in transactions_raw.description]

        return [{ names[i]: trans[i] for i in range(len(names))} for trans in transactions_raw]


    def get_income_statement_line_items(self, *, include_calculated_line_items=True):
        query = "SELECT Description FROM IncomeStatementLineItem"
        if not include_calculated_line_items:
            query += " WHERE IsCalculatedLineItem = 0"

        return [line_items[0] for line_items in self._connection.execute(query)]


    def init_financial_tables(self):
        """Creates tables for the db on first run."""

        for file_path in [
            'sql/CreateInsert_IncomeStatementLineItem.sql',
            'sql/CreateInsert_FinancialTransactionType.sql',
            'sql/CreateInsert_FinancialTransaction.sql'
        ]:
            self.execute_sql_file(file_path, as_script=True)

        self.close_connection()

