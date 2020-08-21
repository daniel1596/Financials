CREATE TABLE FinancialTransactionType (
  FinancialTransactionTypeID INTEGER PRIMARY KEY,
  IncomeStatementLineItemID INTEGER NOT NULL, -- e.g. Operating Expense
  Category TEXT NOT NULL,
  
  -- not sure if both of these columns are needed... wouldn't it all display on the balance sheet, even if not on the income statement?
  IsDisplayedOnIncomeStatement INTEGER NOT NULL,
  IsDisplayedOnBalanceSheet INTEGER NOT NULL
)

-- Using the "WITH" clause maybe? Might try this. See https://stackoverflow.com/a/56179189
-- WITH OpEx_ID AS (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses'),
--   OpIncome_ID AS (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Income')
-- Not sure on the syntax here for selecting from the WITH statement... hmm. Do I do SELECT IncomeStatementLineItemID FROM OpEx_ID? That's hardly much better...

INSERT INTO FinancialTransactionType (IncomeStatementLineItemID, Category, IsDisplayedOnBalanceSheet, IsDisplayedOnIncomeStatement)
VALUES

-- Not sure on the syntax here for selecting from the WITH statement... hmm. It may not be that worth it. Should the inserting be done from Python? Hmm...
-- I like the idea of using raw SQL but maybe inserts should just come from Python if it'll be easier. I don't know.
-- Python could always attempt to run SQL at the command line but I don't know if that would be a good idea.
-- Actually maybe all the inserting should be done from within the app anyway? Might be more debuggable? Hmm.

('Groceries', (SELECT IncomeStatementLineItemID FROM IncomeStatementLineItem WHERE Description = 'Operating Expenses'), 0, 0, 1),
-- ('Housing/Rent/??', 0, 0, 1)