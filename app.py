from flask import Flask, render_template, request
from jsonpickle import encode

from py.financials.Quarter import Quarter
from py.financials.balance_sheet.BalanceSheetFactory import balance_sheet
from py.financials.income_statement.IncomeStatementCategory import income_statement_categories
from py.scripting.IncomeStatementFactory import IncomeStatementFactory
from py.view_models.IncomeStatementsViewModel import IncomeStatementsViewModel

app = Flask(__name__)

"""
A general app note - I think we only want the financial activities to be stored in the database.
On the back-end, Python can create the income statement(s) in-memory and expose them at a particular API endpoint.
Vue and Tabulator can take over as far as the display goes.

I will probably stick with Python to calculate all row values, since very little data is going to be passed to the
  front-end, no matter how many activities are added/processed server-side.  
"""

@app.route('/api/income_statements')
def generate_income_statements():
    starting_year = request.args.get('starting_year', default=2020, type=int)
    starting_quarter_number = request.args.get('starting_quarter', default=None, type=int)
    analysis_type = request.args.get('analysisType', default=None, type=str)

    starting_quarter = next((q for q in Quarter if q.number == starting_quarter_number), None)

    if analysis_type == 'QOQ' and starting_quarter:
        income_statements = IncomeStatementFactory.generate_QOQ_statements(starting_year, starting_quarter)
    elif analysis_type == 'YOY' and starting_quarter:
        income_statements = IncomeStatementFactory.generate_YOY_statements(starting_year, starting_quarter)
    elif analysis_type == 'Yearly':
        income_statements = IncomeStatementFactory.generate_yearly_statements(starting_year)
    else:
        income_statements = [] # error situation; should not happen

    income_statement_view_model = IncomeStatementsViewModel(income_statements)

    # in encode(), "unpicklable" set to False removes "py/object" fields
    return encode(income_statement_view_model, unpicklable=False)


@app.route('/')
def hello_world():
    return render_template('index.html', balance_sheet=balance_sheet,
                           income_statement_categories=income_statement_categories)


if __name__ == '__main__':
    app.run(debug=True)
