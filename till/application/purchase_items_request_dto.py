from typing import List
from dataclasses import dataclass

from till.application.item_dto import ItemDTO


@dataclass(frozen=True)
class PurchaseItemsRequestDTO:
    items_purchased: List[ItemDTO]
