from enum import Enum, auto

class Transactionstatus(Enum):
    """Represents the status of a transaction"""

    PENDING = auto()

    PROCESSED = auto()

    FAILED = auto()