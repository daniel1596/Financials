from dataclasses import dataclass
from typing import List

from py.financials.balance_sheet.Assets import Asset
from py.financials.balance_sheet.Liability import Liability


@dataclass(init=True)
class BalanceSheet:
    assets: List[Asset]
    liabilities: List[Liability]
