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
-- I wish we had variables here... ugh. Not sure I'd want to do this in Python though.
('Bank Account Interest', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Interest Income')),
('Groceries', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses' LIMIT 1)),
('Housing', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses' LIMIT 1)),
('Healthcare', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses' LIMIT 1)),
('Utilities', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses' LIMIT 1))

-- Other ideas: books, car maintenance, clothing, dining, education, entertainment, exercise, gifts, grocery,
-- hygiene/gromming/personal care maybe?, household supplies, misc, travel (includes lodging)


-- Using the "WITH" clause maybe? Might try this. See https://stackoverflow.com/a/56179189
-- WITH OpEx_ID AS (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses'),
--   OpIncome_ID AS (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Income')
-- Not sure on the syntax here for selecting from the WITH statement... hmm. Do I do SELECT IncomeStatementLineItemID FROM OpEx_ID? That's hardly much better...
-- Or should the inserting be done from Python?
-- I like the idea of using raw SQL but maybe inserts should just come from Python if it'll be easier. I don't know.
-- Python could always attempt to run raw SQL through the SQLite package.
-- Actually maybe all the inserting should be done from within the app anyway? Might be more debuggable? Hmm.

