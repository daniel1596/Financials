from datetime import date

from py.financials.balance_sheet.Assets import Asset
from py.financials.income_statement.IncomeStatementCategory import IncomeStatementCategory


class FinancialActivity:
    """Base class (I think) for transactions, capital gains (realized), expenses, etc."""
    def __init__(self, amount: float, date_: date, income_statement_category: IncomeStatementCategory):
        self.amount = amount
        self.date = date_
        self.income_statement_category = income_statement_category

    @property
    def amount_ui(self) -> str:
        """
        Forcing two decimal places for the front-end display.
        The "Expense" subclass will override this to put parentheses around
        """
        return "{:,.2f}".format(self.amount)


class AssetTransfer(FinancialActivity):
    """
    Transferring from one type of asset to another - e.g. stock purchase - with no immediate change in net worth.
    Not sure if I'll do "type" from/to or the actual Asset object. Seems like it should be an actual Asset object.
    """
    def __init__(self, amount: float, date_: date, income_statement_category, asset_from: Asset, asset_to: Asset):
        super(AssetTransfer, self).__init__(amount, date_, income_statement_category)
        self.asset_type_from = asset_from
        self.asset_type_to = asset_to
