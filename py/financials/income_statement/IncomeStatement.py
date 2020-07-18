from typing import List, Optional

from py.financials.Quarter import Quarter
from py.financials.activities.FinancialActivity import FinancialActivity
from py.financials.income_statement.IncomeStatementCategory import RevenueCategory, ExpenseCategory, \
    IncomeStatementCategory
from py.scripting.FinancialActivities import get_financial_activities


class IncomeStatement:
    """
    Just getting something basic down. Can make more complex later.
    TODO should probably map this to a ViewModel
    """

    @property
    def operating_income(self):
        return self.operating_revenue - self.operating_expenses

    @property
    def income_before_taxes(self) -> float:
        return self.operating_income + self.interest_revenue - self.non_operating_expenses

    @property
    def net_income(self) -> float:
        """This is equal to after-tax income because I have no "Minority Interest and Equity in Affiliates"."""
        return self.income_before_taxes - self.income_tax_loss

    @property
    def net_income_ui(self) -> str:
        # This is not fully DRY with the Expense class amount_ui but can fix later.
        # I don't know that the Expenses (subclass of FinancialActivity) will actually need the parentheses... not sure.
        # Or it might be moved to more of a general-purpose utility class later.
        return self._add_parentheses_if_negative(self.net_income)

    @property
    def quarter_ui(self) -> str:
        return self.quarter.name if self.quarter else ""

    def __init__(self, activities: List[FinancialActivity], year: int, quarter: Optional[Quarter] = None):
        """Create an income statement from a pre-filtered list of financial activities."""
        self.year = year
        self.quarter = quarter
        self.operating_revenue = self._sum_amount_by_category(activities, RevenueCategory.OPERATING)
        self.operating_expenses = self._sum_amount_by_category(activities, ExpenseCategory.OPERATING)
        self.interest_revenue = self._sum_amount_by_category(activities, RevenueCategory.INTEREST)
        self.non_operating_expenses = self._sum_amount_by_category(activities, ExpenseCategory.NON_OPERATING)
        self.income_tax_loss = self._sum_amount_by_category(activities, ExpenseCategory.INCOME_TAX)
        self.gains = 0
        self.losses = 0

    @staticmethod
    def generate(year: int, quarter: Optional[Quarter] = None) -> 'IncomeStatement':
        activities = get_financial_activities(year, quarter)
        return IncomeStatement(activities, year, quarter)

    def _add_parentheses_if_negative(self, amount: float) -> str:
        if amount >= 0:
            return "{:,.2f}".format(amount)

        return "(" + "{:,.2f}".format(abs(amount)) + ")"

    def _sum_amount_by_category(self, activities: List[FinancialActivity], category: IncomeStatementCategory):
        return sum(act.amount for act in activities if act.income_statement_category == category)
