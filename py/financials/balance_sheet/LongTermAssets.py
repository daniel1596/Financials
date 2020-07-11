from py.financials.balance_sheet.Assets import LongTermAsset, DebtSecurity


class LongTermInvestment(LongTermAsset):
    """Securities that will not or cannot be liquidated in the next year."""
    pass

class LongTermEquitySecurity(LongTermInvestment): pass
class LongTermDebtSecurity(LongTermInvestment, DebtSecurity): pass

class RetirementAccount(LongTermEquitySecurity):
    is_roth: bool

class RothIRA(RetirementAccount): is_roth = True
class Roth401k(RetirementAccount): is_roth = True

class LongTermSavingsBond(LongTermDebtSecurity):
    """Treasury bonds or corporate bonds"""
    pass

class LongTermCD(LongTermDebtSecurity): pass