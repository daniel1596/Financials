from typing import List, Optional

from py.financials.Quarter import Quarter
from py.financials.activities.FinancialActivity import FinancialActivity
from py.financials.income_statement.IncomeStatementCategory import RevenueCategory, ExpenseCategory, \
    IncomeStatementCategory
from py.scripting.FinancialActivities import get_financial_activities


class IncomeStatement:
    def __init__(self, activities: List[FinancialActivity]):
        """Create an income statement from a pre-filtered list of financial activities."""
        most_recent_date = max(act.date for act in activities)
        
        self.year = most_recent_date.year
        self.quarter = next(q for q in Quarter if q.includes_month(most_recent_date.month))

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
        

    @staticmethod
    def generate(year: int, quarter: Optional[Quarter] = None) -> 'IncomeStatement':
        activities = get_financial_activities(year, quarter)
        return IncomeStatement(activities)

    def _sum_amount_by_category(self, activities: List[FinancialActivity], category: IncomeStatementCategory):
        return sum(act.amount for act in activities if act.income_statement_category == category)
