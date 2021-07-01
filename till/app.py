import json
import os

from flask import Flask
from flask import request

from till.application.item_dto import ItemDTO
from till.application.purchase_items_request_dto import PurchaseItemsRequestDTO
from till.application.services.purchase_items import PurchaseItems
from till.integration.topics.purchases_topic import PurchasesTopic


LOGGING_DEBUG_LEVEL = int(os.environ.get("LOGGING_DEBUG_LEVEL", 20))
BROKER_HOST = os.environ.get("BROKER_HOST", "localhost")

purchase_topic = PurchasesTopic(BROKER_HOST)

application = Flask(__name__)


@application.route("/", methods=['GET'])
def get_home():
    return "till-backend"


@application.route("/items_purchase", methods=['POST'])
def post_items_purchase():
    global purchase_topic
    data = json.loads(request.data)
    item_dtos = []
    for item in data["items_purchased"]:
        item_dtos.append(ItemDTO(
            item["sku"], item["amount"]))
    purchase_items_request_dto = PurchaseItemsRequestDTO(item_dtos)

    purchase_items = PurchaseItems(purchase_topic)
    purchase_items(purchase_items_request_dto)
    return {
        "msg": "Item Purchase was accepted"
    }


if __name__ == "__main__":
    application.run()
