from datetime import date

from py.financials.activities.PurchaseCategory import PurchaseCategory
from py.financials.activities.expenses.Expense import Expense
from py.financials.income_statement.IncomeStatementCategory import ExpenseCategory


class OperatingExpense(Expense):
    """
    Base class for operating expenses - food, housing, utilities, and other essentials.
    Keep in mind that "operating expense" does not mean "necessary"; one could purchase too expensive
    of a dwelling or spend too much eating out, for example.
    But food and shelter are generally necessary expenditures to operate or sustain life.
    It excludes categories such as travel and entertainment.
    Not sure about education. Probably not technically operating.
    """
    def __init__(self, amount: float, date_: date, purchase_category: PurchaseCategory):
        super().__init__(amount, date_, ExpenseCategory.OPERATING, purchase_category)


class HousingPayment(OperatingExpense):
    def __init__(self, amount: float, date_: date):
        super().__init__(amount, date_, PurchaseCategory.HOUSING)


class RentPayment(HousingPayment):
    pass


class GroceryStorePurchase(OperatingExpense):
    def __init__(self, amount: float, date_: date, income_sheet_category):
        super().__init__(amount, date_, income_sheet_category)
