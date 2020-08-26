class TransactionViewModel:
    def __init__(self, dictionary: dict):
        for k, v in dictionary.items():
            setattr(self, k, v)

        self.DateUI = f"{self.DateYear}-{self.DateMonth}-{self.DateDay}"