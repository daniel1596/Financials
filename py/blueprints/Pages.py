from flask import render_template

from py.financials.balance_sheet.BalanceSheetFactory import balance_sheet
from py.financials.income_statement.IncomeStatementCategory import income_statement_categories
from . import Blueprint

pages = Blueprint("pages", __name__)


@pages.route('/')
def hello_world():
    return render_template('index.html', balance_sheet=balance_sheet,
                           income_statement_categories=income_statement_categories)