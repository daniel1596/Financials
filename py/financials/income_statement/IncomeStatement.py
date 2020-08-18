from typing import List, Optional

from py.financials.Quarter import Quarter
from py.financials.activities.FinancialActivity import FinancialActivity
from py.financials.income_statement.IncomeStatementCategory import RevenueCategory, ExpenseCategory, \
    IncomeStatementCategory
from py.scripting.FinancialActivities import get_financial_activities


class IncomeStatement:
    def __init__(self, year: int, quarter: Optional[Quarter] = None):
        """
        Updated: removed IncomeStatement.generate() as it was not needed to have that method plus this __init__().
        Also, setting the attributes (e.g. self.year = year) should stay in __init__().
        """
        self.year = year
        self.quarter = quarter

        activities = get_financial_activities(year, quarter)
        self.operating_revenue = self._sum_amount_by_category(activities, RevenueCategory.OPERATING)
        self.operating_expenses = self._sum_amount_by_category(activities, ExpenseCategory.OPERATING)
        self.operating_income = self.operating_revenue - self.operating_expenses
        self.interest_revenue = self._sum_amount_by_category(activities, RevenueCategory.INTEREST)
        self.non_operating_expenses = self._sum_amount_by_category(activities, ExpenseCategory.NON_OPERATING)
        self.income_before_taxes = self.operating_income + self.interest_revenue - self.non_operating_expenses
        self.income_tax_loss = self._sum_amount_by_category(activities, ExpenseCategory.INCOME_TAX)
        self.net_income = self.income_before_taxes - self.income_tax_loss
        self.gains = 0
        self.losses = 0

    @property
    def date_ui(self) -> str:
        if not self.quarter:
            return str(self.year)

        return f"{self.quarter.name} {self.year}"

    def _sum_amount_by_category(self, activities: List[FinancialActivity], category: IncomeStatementCategory):
        return sum(act.amount for act in activities if act.income_statement_category == category)
