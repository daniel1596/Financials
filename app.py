from flask import Flask, render_template, request
from jsonpickle import encode

from py.financials.Quarter import Quarter
from py.financials.balance_sheet.BalanceSheetFactory import balance_sheet
from py.financials.income_statement.IncomeStatement import IncomeStatement
from py.financials.income_statement.IncomeStatementCategory import income_statement_categories
from py.scripting.FinancialActivities import get_financial_activities
from py.scripting.IncomeStatementFactory import IncomeStatementFactory
from py.view_models.IncomeStatementsViewModel import IncomeStatementsViewModel

app = Flask(__name__)

"""
A general app note - I think we only want the financial activities to be stored in the database.
On the back-end, Python can create the income statement(s) in-memory and expose them at a particular API endpoint.
Vue can take over from there and Tabulator can probably create the calculated columns.
"""

@app.route('/api/income_statements')
def generate_income_statements():
    starting_year = request.args.get('starting_year', default=2020, type=int)
    starting_quarter_number = request.args.get('starting_quarter', default=3, type=int)
    analysis_type = request.args.get('analysis_type', default='QOQ', type=str) # TODO actually implement this

    starting_quarter = next(q for q in Quarter if q.number == starting_quarter_number)
    
    # this will need some work but we'll get there... should Quarters include the year? I am starting to think so.
    previous_three_quarters = starting_quarter.previous_three_quarters

    income_statements = [
        IncomeStatement(get_financial_activities(starting_year, quarter)) 
        for quarter in [starting_quarter] + previous_three_quarters[0:2]
        # the indexing is necessary because Q4 2020 doesn't have any financial activities in it.
        # but this is just for testing, anyway.
    ]

    income_statement_view_model = IncomeStatementsViewModel(income_statements)

    # in encode(), "unpicklable" set to False removes "py/object" fields
    return encode(income_statement_view_model, unpicklable=False)



@app.route('/')
def hello_world():
    return render_template('index.html', balance_sheet=balance_sheet,
                           income_statement_categories=income_statement_categories)


if __name__ == '__main__':
    app.run(debug=True)
