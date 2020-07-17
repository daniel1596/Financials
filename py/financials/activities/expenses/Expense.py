from datetime import date

from py.financials.activities.FinancialActivity import FinancialActivity
from py.financials.activities.PurchaseCategory import PurchaseCategory
from py.financials.income_statement.IncomeStatementCategory import ExpenseCategory


class Expense(FinancialActivity):
    """
    Any purchase that decreases wealth, generally to purchase goods or services.
    I am not sure about buying big things like cars/houses but those can be dealt with when we get there.
    It seems like those are really more loans or per-month expenses... hmm.
    """
    def __init__(self, amount: float, date_: date, income_sheet_category: ExpenseCategory,
                 purchase_category: PurchaseCategory):
        super().__init__(amount, date_, income_sheet_category)
        self.purchase_category = purchase_category

    @property
    def amount_ui(self) -> str:
        return "(" + super().amount_ui + ")"  # one of the few instances where string formatting isn't more readable