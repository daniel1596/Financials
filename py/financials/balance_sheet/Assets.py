from py.financials.balance_sheet.DebtType import DebtType


class BalanceSheetItem:
    """Base class for assets, liabilities, and shareholder equity."""
    monetary_value: float


class Asset(BalanceSheetItem):
    """Base class for all assets."""
    name: str


class CurrentAsset(Asset):
    """Base class for current assets, which can be converted to cash in one year or less"""
    pass


class LongTermAsset(Asset):
    """Base class for long-term assets, which (or will not) be converted into cash within the next year."""
    pass


class DebtSecurity(Asset):
    """An additional class that can be inherited for short-term and long-term debt securities."""
    debt_type: DebtType


