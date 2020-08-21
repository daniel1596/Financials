-- I think the table should actually be named Transaction, perhaps.
-- Asset transfers (e.g. buying/selling stock) wouldn't show up
-- on an income statement, though they would on a balance sheet.

-- Also, looking in FinancialActivity.py, I notice that all the 
-- AssetTransfer class has in common with its parent class
-- is category (dubious), amount, and date.

-- Dividends are one thing (if not reinvested automatically... hmm),
-- but again, I think that should only show on the balance sheet.
-- Unless they're actually realized as income but mine generally aren't.

-- So, I think a separate table for different kinds of transactions
-- might be in order. Ones that don't actually change net worth,
-- and thus aren't counted under operating expenses.

CREATE TABLE FinancialActivity (
  FinancialActivityID INTEGER PRIMARY KEY,
  Name_ TEXT NOT NULL
)