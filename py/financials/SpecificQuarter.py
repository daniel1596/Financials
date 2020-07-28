from py.financials.Quarter import Quarter


class SpecificQuarter:
    """
    I'm not really sure I love this class... maybe it should get molded into something else?

    Its very presence suggests that perhaps a "quarter" should include the concept of a year in it, but I'm not sure
    on how I want to handle that. After all, theoretically one can speak of a "Q3" as a concept separate from a
    particular year. But in reality, a firm's Q3 results only mean something in the context of a specific Q3.

    Perhaps a separate QuarterType or QuarterNumber enum is what I should rename the current Quarter class?
    """
    def __init__(self, year: int, quarter: Quarter):
        self.year = year
        self.quarter = quarter
