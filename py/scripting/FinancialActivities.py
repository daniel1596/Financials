from datetime import date
from typing import List, Optional

from py.financials.Quarter import Quarter
from py.financials.activities.expenses.OperatingExpenses import OperatingExpense
from py.financials.activities.FinancialActivity import FinancialActivity
from py.financials.activities.PurchaseCategory import PurchaseCategory
from py.financials.activities.revenues.Revenues import InterestIncome


# This variable really should be coming from a db, but maybe one day
_all_financial_activities = [
    OperatingExpense(50, date(2020, 7, 13), PurchaseCategory.MEDICAL),
    OperatingExpense(53.33, date(2020, 7, 13), PurchaseCategory.UTILITIES),  # Internet
    InterestIncome(40.91, date(2020, 6, 30)),
    InterestIncome(47.74, date(2020, 5, 29)),
    InterestIncome(49.5, date(2020, 4, 30)),
    InterestIncome(52.57, date(2020, 3, 31))
]


def get_financial_activities(year: int = None, quarter: Optional[Quarter] = None) -> List[FinancialActivity]:
    """
    Returns financial activities, generally within a specified period
    :return: The financial activites within the timeframe (or all if no timeframe is specified)
    """
    if not year:
        return _all_financial_activities  # can't really have a quarter without a year

    activities_this_year = [act for act in _all_financial_activities if act.date.year == year]

    if not quarter:
        return activities_this_year

    return [act for act in activities_this_year if quarter.includes_month(act.date.month)]


