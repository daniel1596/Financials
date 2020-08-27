from typing import List

from py.database.FinancialDatabaseHelper import FinancialDatabaseHelper
from py.models.IncomeStatement import IncomeStatement


class IncomeStatementsViewModel:
    def __init__(self, income_statements: List[IncomeStatement]):
        self.dates = [statement.date_ui for statement in income_statements]

        line_item_names = FinancialDatabaseHelper().get_income_statement_line_items()
        self.line_items = [
            dict({ 'field': line_item_name }, **{
                f'value{i}': IncomeStatementsViewModel.display_numeric_value(statement.line_items[line_item_name])
                for i, statement
                in enumerate(income_statements)
            })
            for line_item_name in line_item_names
        ]


    @staticmethod
    def display_numeric_value(amount: float) -> str:
        amount_two_decimal_places = "{:,.2f}".format(abs(amount))

        if amount >= 0:
            return amount_two_decimal_places

        return "(" + amount_two_decimal_places + ")"
