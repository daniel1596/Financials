from enum import Enum, auto


class PurchaseCategory(Enum):
    # could combine gas, car other into "vehicle maintenance"...
    # that's what Citi does, but I'm not so sure.
    # However, I feel like it would be a strength, not a weakness,
    # To have more categories rather than fewer
    
    BOOKS = auto()
    CAR_MAINTENANCE = auto()
    # CERTIFICATE_OF_DEPOSIT = auto()
    CLOTHING = auto()
    DINING = auto()
    EDUCATION = auto()
    ENTERTAINMENT = auto()
    EXERCISE = auto()
    GAS = auto()
    GIFTS = auto()
    GROCERY = auto()
    GROOMING_HYGIENE = auto()
    HOUSEHOLD_SUPPLIES = auto()
    HOUSING = auto() # does this include lodging e.g. hotels?
    MEDICAL = auto()
    MISC = auto()
    TRAVEL = auto() # or do hotels go in this category? hmm.    
    UTILITIES = auto()
    # STOCK = auto() #? I'm not sure about this one. This is more of a transfer of assets from one type to another.
