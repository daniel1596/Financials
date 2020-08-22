from flask import request

from . import *
from ..financials.Quarter import Quarter
from ..scripting.IncomeStatementFactory import IncomeStatementFactory
from ..view_models.IncomeStatementsViewModel import IncomeStatementsViewModel

api = Blueprint("api", __name__, url_prefix="/api")


@api.route('/income_statements')
def generate_income_statements():
    starting_year = request.args.get('starting_year', default=2020, type=int)
    starting_quarter_number = request.args.get('starting_quarter', default=None, type=int)
    analysis_type = request.args.get('analysisType', default=None, type=str)
    column_count = request.args.get('columnCount', default=4, type=int)

    starting_quarter = next((q for q in Quarter if q.number == starting_quarter_number), None)

    if analysis_type == 'QOQ' and starting_quarter:
        income_statements = IncomeStatementFactory.generate_QOQ_statements(starting_year, starting_quarter, column_count)
    elif analysis_type == 'YOY' and starting_quarter:
        income_statements = IncomeStatementFactory.generate_YOY_statements(starting_year, starting_quarter, column_count)
    elif analysis_type == 'Yearly':
        income_statements = IncomeStatementFactory.generate_yearly_statements(starting_year, column_count)
    else:
        income_statements = [] # error situation; should not happen

    income_statement_view_model = IncomeStatementsViewModel(income_statements)

    # in encode(), "unpicklable" set to False removes "py/object" fields
    return encode(income_statement_view_model, unpicklable=False)