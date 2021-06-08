from dataclasses import dataclass

from till.core.interfaces.purchases_topic import PurchasesTopicInterface
from till.core.purchase import Purchase


@dataclass(frozen=True)
class PurchaseEvent:
    sku: str
    unit: str
    count: int

    @classmethod
    def from_purchase(Cls, purchase: Purchase):
        return Cls(purchase.sku, purchase.unit, purchase.count)


class PurchasesTopic(PurchasesTopicInterface):

    def emit_purchase(self, purchase: Purchase):
        purchase_event = PurchaseEvent.from_purchase(purchase)
        print("This would now send: \n" + str(purchase_event))
