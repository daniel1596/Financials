from flask import Flask, render_template

from py.financials.balance_sheet.BalanceSheetFactory import balance_sheet
from py.scripting.FinancialActivities import get_financial_activities
from py.scripting.IncomeStatementFactory import generate_income_statement

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', balance_sheet=balance_sheet,
                           income_statement=generate_income_statement(2020),
                           financial_activities=get_financial_activities())


if __name__ == '__main__':
    app.run()
