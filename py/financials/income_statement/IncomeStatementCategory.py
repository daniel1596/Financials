from enum import Enum, auto


class IncomeStatementCategory:
    """Base class for categories of the income statement. Revenues and expenses can have the actual income."""
    pass

"""
 Note - I'm not sure if these should be two separate enums or not
 I feel like there will be some things that will be expenses vs revenues but I'm not sure
"""

class ExpenseCategory(IncomeStatementCategory):
    INTEREST = auto()
    OPERATING = auto()


class RevenueCategory(IncomeStatementCategory, Enum):
    INTEREST = auto()
    OPERATING = auto()
