from py.financials.SpecificQuarter import SpecificQuarter
from py.financials.Quarter import Quarter
from py.financials.income_statement.IncomeStatement import IncomeStatement


class IncomeStatementFactory:
    @staticmethod
    def generate_QOQ_statements(starting_year: int, starting_quarter: Quarter):
        # I wish there were an easier way to do this - this was a little complex but it worked out
        last_year = starting_year - 1

        years_and_quarters = [SpecificQuarter((last_year if q.number > starting_quarter.number else starting_year), q) for q in Quarter]
        years_and_quarters_sorted = sorted(years_and_quarters, key=lambda yq: (yq.year, yq.quarter.number), reverse=True)

        return [IncomeStatement.generate(yq.year, yq.quarter) for yq in years_and_quarters_sorted]

    @staticmethod
    def generate_YOY_statements(starting_year: int, starting_quarter: Quarter):
        return [
            IncomeStatement.generate(starting_year, starting_quarter),
            IncomeStatement.generate(starting_year - 1, starting_quarter),
            IncomeStatement.generate(starting_year - 2, starting_quarter),
            IncomeStatement.generate(starting_year - 3, starting_quarter)
        ]

    @staticmethod
    def generate_yearly_statements(starting_year: int):
        return [
            IncomeStatement.generate(starting_year),
            IncomeStatement.generate(starting_year - 1),
            IncomeStatement.generate(starting_year - 2),
            IncomeStatement.generate(starting_year - 3)
        ]
