from dataclasses import dataclass


@dataclass(frozen=True)
class Purchase:
    sku: str
    amount: int
