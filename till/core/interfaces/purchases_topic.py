from abc import ABC, abstractmethod

from till.core.purchase import Purchase


class PurchasesTopicInterface(ABC):

    @abstractmethod
    def emit_purchase(self, purchase: Purchase):
        pass
