from py.financials.balance_sheet.Assets import CurrentAsset, DebtSecurity


class CashOrEquivalent(CurrentAsset): pass

class BankAccount(CashOrEquivalent): pass
class SavingsAccount(BankAccount): pass
class CheckingAccount(BankAccount): pass

class MarketableSecurity(CashOrEquivalent): pass
class MarketableEquitySecurity(MarketableSecurity): pass
class MarketableDebtSecurity(MarketableSecurity, DebtSecurity):
    """any short-term bond issued by a public company held by another company"""
    pass
