from dataclasses import dataclass


@dataclass(frozen=True)
class ItemDTO:
    sku: str
    unit: str
    count: int
