from enum import Enum, auto

class AccountStatus(Enum):
    """Represents the status of a bank account"""

    ACTIVE = auto()

    INACTIVE = auto()

    CLOSED = auto()

    FROZEN = auto()