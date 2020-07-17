from datetime import date

from py.financials.activities.FinancialActivity import FinancialActivity
from py.financials.activities.PurchaseCategory import PurchaseCategory


class Expense(FinancialActivity):
    """
    Any purchase that decreases wealth, generally to purchase goods or services.
    I am not sure about buying big things like cars/houses but those can be dealt with when we get there.
    It seems like those are really more loans or per-month expenses... hmm.
    """
    def __init__(self, amount: float, date_: date, category: PurchaseCategory):
        super(Expense, self).__init__(amount * -1, date_)
        self.category = category


class HousingPayment(Expense):
    def __init__(self, amount: float, date_: date):
        super(HousingPayment, self).__init__(amount, date_, PurchaseCategory.HOUSING)


class RentPayment(HousingPayment):
    pass


class GroceryStorePurchase(Expense):
    def __init__(self, amount: float, date_: date):
        super().__init__(amount, date_, PurchaseCategory.GROCERY)
