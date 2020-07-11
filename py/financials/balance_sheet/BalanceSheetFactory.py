from py.financials.balance_sheet.BalanceSheet import BalanceSheet
from py.financials.balance_sheet.LongTermAssets import RothIRA

balance_sheet = BalanceSheet(assets=[
    RothIRA()
], liabilities=[])