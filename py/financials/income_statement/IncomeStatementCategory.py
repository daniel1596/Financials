from enum import Enum, auto


class IncomeStatementCategory:
    """Base class for categories of the income statement. Revenues and expenses can have the actual income."""
    def __init__(self, title: str, attribute: str):
        self.title = title
        self.attribute = attribute


class ExpenseCategory(IncomeStatementCategory, Enum):
    INCOME_TAX = ('Income tax loss (gain)', 'income_tax_loss')
    # INTEREST = ('')  # I guess I could add this at some point, if I were to have any
    NON_OPERATING = ('Non-operating expenses', 'non_operating_expenses')
    OPERATING = ('Operating expenses', 'operating_expenses')


class ProfitCategory(IncomeStatementCategory, Enum):
    """Some of these terms could be used interchangeably with income, like 'Gross profit' vs 'Gross income'... oh well"""
    BEFORE_TAXES = ('Income before taxes', 'income_before_taxes')
    NET_INCOME = ('Net income', 'net_income')
    OPERATING = ('Operating income', 'operating_income')

class RevenueCategory(IncomeStatementCategory, Enum):
    INTEREST = ('Interest revenue', 'interest_revenue')
    OPERATING = ('Revenue', 'operating_revenue')


income_statement_categories = [
    # In order of how they will appear on the balance sheet, top line to bottom
    RevenueCategory.OPERATING,
    # For personal finance purposes, gross profit = revenue because there are no COGS. So it's not a separate line item.
    ExpenseCategory.OPERATING,
    ProfitCategory.OPERATING,
    RevenueCategory.INTEREST,
    ExpenseCategory.NON_OPERATING,
    ProfitCategory.BEFORE_TAXES,
    ExpenseCategory.INCOME_TAX,
    ProfitCategory.NET_INCOME
]