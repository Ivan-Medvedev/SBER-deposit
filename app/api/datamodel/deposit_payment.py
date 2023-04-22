from datetime import date
from dataclasses import dataclass


@dataclass
class DepositPayment:
    date: date
    amount: float
