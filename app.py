from flask import Flask, render_template, request
from jsonpickle import encode

from py.financials.Quarter import Quarter
from py.financials.balance_sheet.BalanceSheetFactory import balance_sheet
from py.financials.income_statement.IncomeStatement import IncomeStatement
from py.financials.income_statement.IncomeStatementCategory import income_statement_categories
from py.scripting.IncomeStatementFactory import IncomeStatementFactory

app = Flask(__name__)


@app.route('/api/income_statement')
def generate_income_statement():
    year = request.args.get('year', default=2020, type=int)
    quarter_number = request.args.get('quarter', default=3, type=int)

    quarter = next((q for q in Quarter if q.number == quarter_number), None)

    # The query string parameters work! But again, todo should be using a ViewModel for this
    return encode(IncomeStatement.generate(year, quarter if quarter else None))
    # return jsonify(IncomeStatement.generate(2020, quarter if quarter else None)) # this errored more easily.


@app.route('/')
def hello_world():
    return render_template('index.html', balance_sheet=balance_sheet,
                           income_statement_categories=income_statement_categories)


if __name__ == '__main__':
    app.run()
