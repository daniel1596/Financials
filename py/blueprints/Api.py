from flask import request

from . import *
from .response.CustomResponse import CustomResponse
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

@api.route('/transactions/checkUpload', methods=['POST'])
def check_upload():
    files_key = 'checkExcelFile'
    if files_key not in request.files:
        return CustomResponse.error('A programming error occurred.')

    file = request.files[files_key]

    file_extension = file.filename.split('.')[-1]
    if not file_extension.startswith('xls'):
        return CustomResponse.error('Did not work out')

    # Perform the actual file import here - probably calling a helper function.

    return CustomResponse.success('File format looks great.')


@api.route('/transactions/upload', methods=['POST'])
def upload_transactions():
    files_key = 'importExcelFile'
    if files_key not in request.files:
        return CustomResponse.error('A programming error occurred.')

    return CustomResponse.success('It worked. View the table to see your transactions.')