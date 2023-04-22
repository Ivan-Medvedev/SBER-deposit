from datetime import date
from dataclasses import dataclass


@dataclass
class DepositTerms:
    amount: int
    periods: int
    rate: float
    date: date
