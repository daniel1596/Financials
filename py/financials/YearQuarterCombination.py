from py.financials.Quarter import Quarter


class YearQuarterCombination:
    """I'm not really sure I love this class... maybe it should get molded into something else?"""
    def __init__(self, year: int, quarter: Quarter):
        self.year = year
        self.quarter = quarter
