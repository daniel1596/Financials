from datetime import date

from py.financials.activities.FinancialActivity import FinancialActivity
from py.financials.income_statement.IncomeStatementCategory import RevenueCategory


class Revenue(FinancialActivity):
    """Base class for revenues"""
    def __init__(self, amount: float, date_: date, income_statement_category: RevenueCategory):
        super().__init__(amount, date_, income_statement_category)


class Paycheck(Revenue):
    """Earned revenues for employment"""
    pass


class InterestIncome(Revenue):
    def __init__(self, amount: float, date_: date):
        super().__init__(amount, date_, RevenueCategory.INTEREST)