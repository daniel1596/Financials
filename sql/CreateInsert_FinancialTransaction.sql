-- All transactions, including all dividends and stock purchases, will show up here.

CREATE TABLE FinancialTransaction (
  FinancialTransactionID INTEGER PRIMARY KEY,
  FinancialTransactionTypeID INTEGER NOT NULL,
  Amount REAL NOT NULL,

  -- I believe storing the dates in this way is good. It is fully agnostic of how the data is displayed on the front-end.
  -- It won't go out of style, unless I choose not to utilize the day of the transaction at all.
  -- In such a case, this structure would be preferred; one could easily make the "day" field nullable.
  DateYear INTEGER NOT NULL,
  DateMonth INTEGER NOT NULL,
  DateDay INTEGER NOT NULL
);

-- test data - this won't stay here forever, but is helpful for now.
-- eventually all the data will be done through importing I presume.
INSERT INTO FinancialTransaction (FinancialTransactionTypeID, Amount, DateYear, DateMonth, DateDay)
VALUES
((SELECT FinancialTransactionTypeID FROM FinancialTransactionType WHERE Category = 'Healthcare'), 50, 2020, 7, 13),
((SELECT FinancialTransactionTypeID FROM FinancialTransactionType WHERE Category = 'Utilities'), 53.33, 2020, 7, 13)


--    InterestIncome(40.91, date(2020, 6, 30)),
--    InterestIncome(47.74, date(2020, 5, 29)),
--    InterestIncome(49.5, date(2020, 4, 30)),
--    InterestIncome(52.57, date(2020, 3, 31))