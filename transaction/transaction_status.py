from enum import Enum, auto

class TransactionStatus(Enum):
    """Represents the status of a transaction"""

    PENDING = auto()

    PROCESSED = auto()

    FAILED = auto()