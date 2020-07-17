from typing import Optional

from py.financials.income_statement.IncomeStatement import IncomeStatement
from py.financials.Quarter import Quarter
from py.scripting.FinancialActivities import get_financial_activities


def generate_income_statement(year: int, quarter: Optional[Quarter] = None) -> IncomeStatement:
    """I'm not at all certain that this factory is necessary. Hmm."""
    activities = get_financial_activities(year, quarter)
    return IncomeStatement(activities)
