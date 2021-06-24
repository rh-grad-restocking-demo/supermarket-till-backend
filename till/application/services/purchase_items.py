from till.core.purchase import Purchase
from till.core.interfaces.purchases_topic import PurchasesTopicInterface
from till.application.purchase_items_request_dto import PurchaseItemsRequestDTO


class PurchaseItems:

    def __init__(self, purchases_topic: PurchasesTopicInterface):
        self._purchases_topic = purchases_topic

    def __call__(self, dto: PurchaseItemsRequestDTO):
        for item in dto.items_purchased:
            purchase = Purchase(
                sku=item.sku,
                price=item.price,
                amount=item.amount)
            self._purchases_topic.emit_purchase(purchase)
