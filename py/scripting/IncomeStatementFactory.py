from typing import List

from py.financials.SpecificQuarter import SpecificQuarter
from py.financials.Quarter import Quarter
from py.financials.income_statement.IncomeStatement import IncomeStatement


class IncomeStatementFactory:
    # If I need anything to be an instance of this class, I can make these methods @classmethods,
    # so I can use e.g. the cls._year_count inside the methods.

    @staticmethod
    def generate_QOQ_statements(starting_year: int, starting_quarter: Quarter, column_count: int):
        """
        For now, I am only doing 4 QOQ statements, regardless of the value of column_count.
        Currently, the option to change the column count is hidden in the UI. But that's inconsistent and limits
        the functionality. So one day I'd like to tackle that.
        """

        # I wish there were an easier way to do this - this was a little complex but it worked out
        last_year = starting_year - 1

        years_and_quarters = [SpecificQuarter((last_year if q.number > starting_quarter.number else starting_year), q) for q in Quarter]
        years_and_quarters_sorted = sorted(years_and_quarters, key=lambda yq: (yq.year, yq.quarter.number), reverse=True)

        return [IncomeStatement(yq.year, yq.quarter) for yq in years_and_quarters_sorted]

    @staticmethod
    def generate_YOY_statements(starting_year: int, starting_quarter: Quarter, column_count: int):
        return [IncomeStatement(year, starting_quarter) 
            for year in IncomeStatementFactory._get_x_years_starting_at(starting_year, column_count)
        ]
    
    @staticmethod
    def generate_yearly_statements(starting_year: int, column_count: int):
        return [IncomeStatement(year) 
            for year in IncomeStatementFactory._get_x_years_starting_at(starting_year, column_count)
        ]

    @staticmethod
    def _get_x_years_starting_at(starting_year: int, x: int) -> List[int]:
        # the Python range() "stop" point is exclusive, so this is how math works out
        # e.g. with params (2020, 4), the range_stop will be 2016 - but this exclusive,
        # so the return value will be [2020, 2019, 2018, 2017], which is correct.
        range_stop = starting_year - x

        return list(range(starting_year, range_stop,  -1))