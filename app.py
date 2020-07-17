from flask import Flask, render_template

from py.financials.Quarter import Quarter
from py.financials.balance_sheet.BalanceSheetFactory import balance_sheet
from py.financials.income_statement.IncomeStatement import IncomeStatement
from py.scripting.FinancialActivities import get_financial_activities

app = Flask(__name__)

@app.route('/api/income_statement')
def generate_income_statement()
    # TODO make year and quarter query string parameters here
    return IncomeStatement.generate(2020, Quarter.Q3)


@app.route('/')
def hello_world():
    return render_template('index.html', balance_sheet=balance_sheet,
                           income_statement=IncomeStatement.generate(2020, Quarter.Q3),
                           financial_activities=get_financial_activities())


if __name__ == '__main__':
    app.run()
