CREATE TABLE FinancialTransactionType (
  FinancialTransactionTypeID INTEGER PRIMARY KEY,
  IncomeStatementLineItemID INTEGER NOT NULL, -- e.g. Operating Expense
  Category TEXT NOT NULL,
  FOREIGN KEY("IncomeStatementLineItemID") REFERENCES "IncomeStatementLineItem" ("IncomeStatementLineItemID")

  -- not sure if these columns are needed...
  -- IsDisplayedOnIncomeStatement INTEGER NOT NULL
  -- IsDisplayedOnBalanceSheet INTEGER NOT NULL
);

INSERT INTO FinancialTransactionType (Category, IncomeStatementLineItemID)
VALUES
('Groceries', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses' LIMIT 1))
-- ('Housing/Rent/??', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses' LIMIT 1))



-- Using the "WITH" clause maybe? Might try this. See https://stackoverflow.com/a/56179189
-- WITH OpEx_ID AS (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses'),
--   OpIncome_ID AS (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Income')
-- Not sure on the syntax here for selecting from the WITH statement... hmm. Do I do SELECT IncomeStatementLineItemID FROM OpEx_ID? That's hardly much better...
-- Or should the inserting be done from Python?
-- I like the idea of using raw SQL but maybe inserts should just come from Python if it'll be easier. I don't know.
-- Python could always attempt to run raw SQL through the SQLite package.
-- Actually maybe all the inserting should be done from within the app anyway? Might be more debuggable? Hmm.

