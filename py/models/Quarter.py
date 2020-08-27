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
        """
        This method looks kind of nice, but is unused. Is it needed?
        After all, the "previous quarters" bit really is only useful in the context of particular years...
        e.g. to tell the computer Q1 follows Q4 is really only helpful when saying after Q1 2020 comes Q4 2019.
        """
        previous_quarters_mapping = {
            Quarter.Q4: [Quarter.Q3, Quarter.Q2, Quarter.Q1],
            Quarter.Q3: [Quarter.Q2, Quarter.Q1, Quarter.Q4],
            Quarter.Q2: [Quarter.Q1, Quarter.Q4, Quarter.Q3],
            Quarter.Q1: [Quarter.Q4, Quarter.Q3, Quarter.Q2]
        }

        return previous_quarters_mapping[self]

    def includes_month(self, month: int) -> bool:
        return month in range(self.month_first, self.month_last + 1)

    @classmethod
    def descending(cls, *, start: int=None, end: int=None) -> List['Quarter']:
        quarters_filtered = (q for q in Quarter if (not end or q.number >= end) and (not start or q.number <= start))
        return sorted(quarters_filtered, key=lambda q: q.number, reverse=True)

    @staticmethod
    def matching_number(quarter_number: int) -> 'Quarter':
        return next((q for q in Quarter if q.number == quarter_number), None)