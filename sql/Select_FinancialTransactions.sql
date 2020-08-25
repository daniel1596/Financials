SELECT ft.Amount, ftt.Category
FROM FinancialTransaction ft
	INNER JOIN FinancialTransactionType ftt ON ftt.FinancialTransactionTypeID=ft.FinancialTransactionTypeID