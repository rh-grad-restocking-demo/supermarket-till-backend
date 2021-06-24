from dataclasses import dataclass


@dataclass(frozen=True)
class ItemDTO:
    sku: str
    price: int
    amount: int
