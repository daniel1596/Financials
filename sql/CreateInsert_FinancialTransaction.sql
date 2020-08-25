-- All transactions, including all dividends and stock purchases, will show up here.

CREATE TABLE FinancialTransaction (
  FinancialTransactionID INTEGER PRIMARY KEY,
  FinancialTransactionTypeID INTEGER NOT NULL,
  Amount REAL NOT NULL

  -- I keep wanting to specify the "other party" or "transaction partner", but I don't know
  -- if that's something I need to be worrying about here. After all, that wouldn't show up
  -- on traditional income statements or balance sheets.
);

-- test data - this won't stay here forever, but is helpful for now.
-- eventually all the data will be done through importing I presume.
INSERT INTO FinancialTransaction (FinancialTransactionTypeID, Amount)
VALUES ((SELECT FinancialTransactionTypeID FROM FinancialTransactionType WHERE Category = 'Groceries'), 6.5)