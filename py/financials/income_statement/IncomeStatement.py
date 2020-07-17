from typing import List

from py.financials.activities.Expenses import Expense
from py.financials.activities.FinancialActivity import FinancialActivity, Paycheck


class IncomeStatement:
    """Just getting something basic down. Can make more complex later."""
    revenue_operating: float = 0
    revenue_non_operating: float = 0
    gains: float = 0

    expenses_primary: float = 0
    expenses_secondary: float = 0
    losses: float = 0

    @property
    def revenue_total(self) -> float:
        return self.revenue_operating + self.revenue_non_operating + self.gains

    @property
    def expenses_total(self) -> float:
        return self.expenses_primary + self.expenses_secondary + self.losses

    @property
    def net_income(self) -> float:
        return self.revenue_total - self.expenses_total

    def __init__(self, activities: List[FinancialActivity]):
        """Create an income statement from a pre-filtered list of financial activities."""
        for activity in activities:
            if isinstance(activity, Expense):
                self.expenses_primary += activity.amount
            elif isinstance(activity, Paycheck):
                self.revenue_operating += activity.amount
