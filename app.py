from flask import Flask, render_template

from py.financials.balance_sheet.BalanceSheetFactory import balance_sheet

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', balance_sheet=balance_sheet, income_statement=None)


if __name__ == '__main__':
    app.run()
