-- Any purchases of financial assets (stocks/CDs/bonds) won't show up on the income statement,
-- but they will show up in this table. The FinancialTransactionType table has that information.

-- The AssetTransfer class from Python doesn't necessitate a table most likely
-- Note that reinvested dividends still do count as a transaction of sorts - even though "automatic",
-- they are taxed by the IRS as income. I just choose to reinvest them back into the stock.

CREATE TABLE FinancialTransaction (
  FinancialTransactionID INTEGER PRIMARY KEY,
  FinancialTransactionTypeID INTEGER NOT NULL,
  Amount REAL NOT NULL
  -- TransactionPartnerID INTEGER NULL? E.g. Kroger, etc.? That's probably too much... but I'll probably have a transaction partner name so...
  -- But wait - that would be suboptimal because Kroger will always be groceries. Right? Or at least a default... 
  -- Well, does medicine/pharmacy stuff fall under the grocery category? I presume so but theoretically it could be separate.
  -- However, paper towels and such that are part of a grocery receipt are not so easy to separate. Hmm.
  -- Not that that's that big of a deal but still.
)