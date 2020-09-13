from typing import Optional

from py.database.FinancialDatabaseHelper import FinancialDatabaseHelper
from py.models.Quarter import Quarter


class IncomeStatement:
    def __init__(self, year: int, quarter: Optional[Quarter] = None):
        """
        Updated: removed IncomeStatement.generate() as it was not needed to have that method plus this __init__().
        Also, setting the attributes (e.g. self.year = year) should stay in __init__().
        """
        self.year = year
        self.quarter = quarter

        db_helper = FinancialDatabaseHelper()
        self.transactions = db_helper.get_financial_transactions(year, quarter, include_income_statement_line_item=True)
        self.line_items = {
            line_item_name: self._sum_amounts_for_line_item(line_item_name)
            for line_item_name
            in db_helper.get_income_statement_line_items(include_calculated_line_items=False)
        }

        # Adding the rest of the fields to the dictionary that are calculated
        # This feels a tad hokey but let's get it working first
        self.line_items['Operating Income'] = self.line_items["Operating Revenue"] - self.line_items["Operating Expenses"]
        self.line_items["Income Before Tax"] = \
            self.line_items['Operating Income'] + self.line_items['Interest Income'] \
            + self.line_items["Investment Income"] - self.line_items["Non-operating Expenses"]

        self.line_items["Net Income"] = self.line_items["Income Before Tax"] - self.line_items["Income Tax Loss (Gain)"]
        self.gains = 0
        self.losses = 0

    @property
    def date_ui(self) -> str:
        if not self.quarter:
            return str(self.year)

        return f"{self.quarter.name} {self.year}"

    def _sum_amounts_for_line_item(self, line_item_description: str):
        """This will be the new method we use going forward"""
        return sum(t["Amount"] for t in self.transactions if t["Description"] == line_item_description)
