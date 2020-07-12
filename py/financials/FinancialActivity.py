from py.financials.PurchaseCategory import PurchaseCategory
from py.financials.balance_sheet.Assets import Asset


class FinancialActivity:
    """Base class (I think) for incomes and expenses"""
    def __init__(self, amount: float):
        self.amount = amount


class Purchase(FinancialActivity):
    """Anything that would constitute an expense in the income statement... should this then just be Expense? Hmm."""
    def __init__(self, amount: float, category: PurchaseCategory):
        super(Purchase, self).__init__(amount)
        self.category = category


class AssetTransfer(FinancialActivity):
    """
    Transferring from one type of asset to another - e.g. stock purchase - with no immediate change in net worth.
    Not sure if I'll do "type" from/to or the actual Asset object. Seems like it should be an actual Asset object.
    """
    def __init__(self, amount: float, asset_from: Asset, asset_type_to: Asset):
        super(AssetTransfer, self).__init__(amount)
        self.asset_type_from = asset_from
        self.asset_type_to = asset_type_to
