from typing import List

from py.financials.income_statement.IncomeStatementCategory import income_statement_categories
from py.financials.income_statement.IncomeStatement import IncomeStatement


class IncomeStatementsViewModel:
    def __init__(self, income_statements: List[IncomeStatement]):
        self.dates = [IncomeStatementsViewModel._get_date_ui_from(statement) for statement in income_statements]
        self.line_items = [IncomeStatementLineItem(field, income_statements) for field in [
            cat.attribute for cat in income_statement_categories
        ]]

    @staticmethod
    def _get_date_ui_from(statement: IncomeStatement) -> str:
        if not statement.quarter:
            return str(statement.year)

        return f"{statement.quarter.name} {statement.year}"


class IncomeStatementLineItem:
    def __init__(self, field: str, income_statements: List[IncomeStatement]):
        self.field = next((cat.title for cat in income_statement_categories if cat.attribute == field), field)
        
        for i, statement in enumerate(income_statements):
            numeric_field_value = getattr(statement, field)
            setattr(self, "value" + str(i), IncomeStatementLineItem.display_numeric_value(numeric_field_value))


    @staticmethod
    def display_numeric_value(amount: float) -> str:
        amount_two_decimal_places = "{:,.2f}".format(abs(amount))
        
        if amount >= 0:
            return amount_two_decimal_places

        return "(" + amount_two_decimal_places + ")"