from math import floor
from functools import reduce
from typing import Final, List

from py.financials.SpecificQuarter import SpecificQuarter
from py.financials.Quarter import Quarter
from py.financials.income_statement.IncomeStatement import IncomeStatement


class IncomeStatementFactory:
    # If I need anything to be an instance of this class, I can make these methods @classmethods,
    # so I can use e.g. the cls._year_count inside the methods.

    @staticmethod
    def generate_QOQ_statements(starting_year: int, starting_quarter: Quarter, column_count: int):
        """
        Generate a variable number of QOQ statements. Logic gets tricky but it works.
        The premise is that there is an "initial/starting" year, "middle" years, and an "ending" year.
        """

        if starting_quarter.number >= column_count:
            # We won't have any quarters outside of the starting year, making this pretty easy
            lowest_quarter_number = starting_quarter.number - column_count + 1
            quarters = Quarter.descending(start=starting_quarter.number, end=lowest_quarter_number)
            return [IncomeStatement(starting_year, q) for q in quarters]

        starting_year_statements = [IncomeStatement(starting_year, q) for q in Quarter.descending(start=starting_quarter.number)]

        statements_remaining = column_count - starting_quarter.number
        quarters_in_year: Final = 4
        year_count_four_statements = floor(statements_remaining / quarters_in_year)
        statement_count_oldest_year = statements_remaining % quarters_in_year

        final_year = starting_year - year_count_four_statements - 1

        middle_statements = [] if not year_count_four_statements else list(reduce(list.__add__, (
            [IncomeStatement(y, q)] for y in range(starting_year - 1, final_year, -1) for q in Quarter.descending()
        )))

        last_statement_quarter = 4 - statement_count_oldest_year + 1  # e.g. if 1 statement final year, this is 4 - 1 + 1
        last_year_statements = [IncomeStatement(final_year, q) for q in Quarter.descending(end=last_statement_quarter)]

        return starting_year_statements + middle_statements + last_year_statements

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