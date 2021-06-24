from __future__ import print_function

import sys
import os
import json
from dataclasses import dataclass
from dataclasses import asdict

from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container

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


class PurchaseEventHandler(MessagingHandler):
    def __init__(self, event: PurchaseEvent):
        super(PurchaseEventHandler, self).__init__()

        self.conn_url = os.getenv('HOST')
        self.address = os.getenv('ADDRESS')
        self.message_body = json.dumps(asdict(event))

    def on_start(self, event):
        conn = event.container.connect(self.conn_url)
        event.container.create_sender(conn, self.address)

    def on_link_opened(self, event):
        print("SEND: Opened sender for target address '{0}'".format
              (event.sender.target.address))

    def on_sendable(self, event):
        message = Message(self.message_body)
        event.sender.send(message)

        print("SEND: Sent message '{0}'".format(message.body))

        event.sender.close()
        event.connection.close()


class PurchasesTopic(PurchasesTopicInterface):

    def emit_purchase(self, purchase: Purchase):
        purchase_event = PurchaseEvent.from_purchase(purchase)
        Container(PurchaseEventHandler(purchase_event)).run()
