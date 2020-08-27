from enum import Enum


class DebtType(Enum):
    CORPORATE = 1  # corporate bonds
    GOVERNMENT = 2  # government bonds or CDs - at least I think CDs fall here?
