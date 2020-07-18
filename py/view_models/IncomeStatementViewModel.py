class IncomeStatementViewModel:
    def _add_parentheses_if_negative(self, amount: float) -> str:
        amount_two_decimal_places = "{:,.2f}".format(abs(amount))
        return amount_two_decimal_places if amount >= 0 else f"({amount_two_decimal_places})"