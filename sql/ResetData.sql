-- This would be useful if I was sharing the application with Dad
-- Note that there is no "truncate table" in SQLite.
-- See https://www.techonthenet.com/sqlite/truncate.php

-- These two lines will be removed, or at least commented out, once we are ready to deploy to production.
-- For debugging purposes, however, I will leave them here. Db schema is still in flux of course.
DELETE FROM IncomeStatementLineItem
DELETE FROM FinancialTransactionType

DELETE FROM FinancialTransaction