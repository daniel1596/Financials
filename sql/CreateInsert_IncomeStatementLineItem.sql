CREATE TABLE IncomeStatementLineItem (
  IncomeStatementLineItemID INTEGER PRIMARY KEY,
  Description TEXT NOT NULL,

  -- If 1, there should be no transactions of this kind in the db. Not sure how to best enforce that though...
  IsCalculatedLineItem INTEGER NOT NULL
);


INSERT INTO IncomeStatementLineItem (Description, IsCalculatedLineItem)
VALUES
('Operating Revenue', 0),
('Operating Expenses', 0), -- there is no COGS or "cost of revenue" so this is just purchases
('Operating Income', 1),
('Interest Income', 0),
('Investment Income', 0),
('Non-operating Expenses', 0),
('Income Before Tax', 1),
('Income Tax Loss (Gain)', 0),
('Net Income', 1)
