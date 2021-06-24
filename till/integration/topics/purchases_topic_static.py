from dataclasses import dataclass

from till.core.interfaces.purchases_topic import PurchasesTopicInterface
from till.core.purchase import Purchase


@dataclass(frozen=True)
class PurchaseEvent:
    sku: str
    price: int
    amount: int

    @classmethod
    def from_purchase(Cls, purchase: Purchase):
        return Cls(purchase.sku, purchase.price, purchase.amount)


class PurchasesTopic(PurchasesTopicInterface):

    def emit_purchase(self, purchase: Purchase):
        purchase_event = PurchaseEvent.from_purchase(purchase)
        print("This would now send: \n" + str(purchase_event))
