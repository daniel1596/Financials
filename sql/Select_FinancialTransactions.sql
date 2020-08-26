SELECT ft.Amount, ftt.Category, ft.DateYear, ft.DateMonth, ft.DateDay
FROM FinancialTransaction ft
	INNER JOIN FinancialTransactionType ftt ON ftt.FinancialTransactionTypeID=ft.FinancialTransactionTypeID