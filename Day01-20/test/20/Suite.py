from enum import Enum


class Suite(Enum):
    """花色"""

    SPADE, HEART, DIAMOND, CLUB = range(4)
