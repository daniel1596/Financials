from enum import Enum, auto


class PurchaseCategory(Enum):
    BOOKS = auto()
    CAR_MAINTENANCE = auto()  # separate from gas?
    CERTIFICATE_OF_DEPOSIT = auto()
    CLOTHING = auto()
    EDUCATION = auto()
    ENTERTAINMENT = auto()
    EXERCISE = auto()
    GAS = auto()
    GIFTS = auto()
    GROCERY = auto()
    GROOMING_HYGIENE = auto()
    HOUSEHOLD_SUPPLIES = auto()
    HOUSING = auto()
    MEDICAL = auto()
    MISC = auto()
    UTILITIES = auto()
    # STOCK = auto() #? I'm not sure about this one. This is more of a transfer of assets from one type to another.
