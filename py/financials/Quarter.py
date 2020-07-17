from enum import Enum


class Quarter(Enum):
    """No need for the fiscal year to differ from the calendar year, at least currently"""
    Q1 = (1, 3)
    Q2 = (4, 6)
    Q3 = (7, 9)
    Q4 = (10, 12)

    def __init__(self, month_first: int, month_last: int):
        self.month_first = month_first
        self.month_last = month_last

    def includes_month(self, month: int) -> bool:
        return month in range(self.month_first, self.month_last + 1)