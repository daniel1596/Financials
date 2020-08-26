from flask import request

from . import *
from .response.CustomResponse import CustomResponse
from ..database.DatabaseMethods import get_financial_transactions
from ..financials.Quarter import Quarter
from ..scripting.IncomeStatementFactory import IncomeStatementFactory
from ..view_models.IncomeStatementsViewModel import IncomeStatementsViewModel
from ..view_models.TransactionViewModel import TransactionViewModel

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


@api.route('/transactions/list')
def list_all_transactions():
    # Technically, I believe we should only have one view-model per page... hmm. Can fix later.
    # Would have to create a separate class to call setattr() in the __init__ method.
    view_models = [TransactionViewModel(t) for t in get_financial_transactions()]

    return encode(view_models, unpicklable=False)


@api.route('/transactions/upload/excel/check', methods=['POST'])
def check_upload():
    if not len(request.files):
        return CustomResponse.error('Please use the "browse" button to upload an Excel file first.')

    files_key = 'checkExcelFile'
    if files_key not in request.files:
        return CustomResponse.error('Could not find the Excel file for processing.')

    excel_file = request.files[files_key]

    file_extension = excel_file.filename.split('.')[-1]
    if not file_extension.startswith('xls'):
        return CustomResponse.error('You must upload either a .xls or .xlsx file.')

    # Perform the actual file import here - probably calling a helper function.

    return CustomResponse.success('File format looks great.')


@api.route('/transactions/upload/excel/import', methods=['POST'])
def upload_transactions():
    files_key = 'importExcelFile'
    if files_key not in request.files:
        return CustomResponse.error('Could not find the Excel file for processing.')

    return CustomResponse.success('The file would have imported if we were actually doing that yet haha. '
        'View the table to see your transactions.')


