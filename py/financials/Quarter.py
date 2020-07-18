from enum import Enum
from typing import List


class Quarter(Enum):
    """No need for the fiscal year to differ from the calendar year, at least currently"""
    Q1 = (1, 1, 3)
    Q2 = (2, 4, 6)
    Q3 = (3, 7, 9)
    Q4 = (4, 10, 12)

    def __init__(self, number: int, month_first: int, month_last: int):
        self.number = number
        self.month_first = month_first
        self.month_last = month_last

    @property
    def previous_three_quarters(self) -> List['Quarter']:
        previous_quarters_mapping = {
            Quarter.Q4: [Quarter.Q3, Quarter.Q2, Quarter.Q1],
            Quarter.Q3: [Quarter.Q2, Quarter.Q1, Quarter.Q4],
            Quarter.Q2: [Quarter.Q1, Quarter.Q4, Quarter.Q3],
            Quarter.Q1: [Quarter.Q4, Quarter.Q3, Quarter.Q2]
        }

        return previous_quarters_mapping[self]

    def includes_month(self, month: int) -> bool:
        return month in range(self.month_first, self.month_last + 1)