from datetime import date

from py.financials.balance_sheet.Assets import Asset


class FinancialActivity:
    """Base class (I think) for transactions, capital gains (realized), expenses, etc."""
    def __init__(self, amount: float, date_: date):
        self.amount = amount
        self.date = date_

    @property
    def amount_ui(self) -> str:
        """Formatting for the front-end, using () over minus signs  """
        decimal_amt = "{:,.2f}".format(abs(self.amount))

        return decimal_amt if self.amount > 0 else f"({decimal_amt})"


class AssetTransfer(FinancialActivity):
    """
    Transferring from one type of asset to another - e.g. stock purchase - with no immediate change in net worth.
    Not sure if I'll do "type" from/to or the actual Asset object. Seems like it should be an actual Asset object.
    """
    def __init__(self, amount: float, date_: date, asset_from: Asset, asset_type_to: Asset):
        super(AssetTransfer, self).__init__(amount, date_)
        self.asset_type_from = asset_from
        self.asset_type_to = asset_type_to


class Revenue(FinancialActivity):
    """Base class for revenues"""
    pass


class Paycheck(Revenue):
    """Earned revenues for employment"""
    pass
