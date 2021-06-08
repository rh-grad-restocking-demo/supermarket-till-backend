from flask import Flask
from flask import request

from till.application.item_dto import ItemDTO
from till.application.purchase_items_request_dto import PurchaseItemsRequestDTO
from till.application.services.purchase_items import PurchaseItems
from till.integration.topics.purchases_topic import PurchasesTopic


wsgi = Flask(__name__)


@wsgi.route("/", methods=['GET'])
def get_home():
    return "This is working."


@wsgi.route("/items_purchase", methods=['POST'])
def post_items_purchase():
    data = request.get_json()
    item_dtos = []
    for item in data["items_purchased"]:
        item_dtos.append(ItemDTO(
            item["sku"], item["unit"], item["count"]))
    purchase_items_request_dto = PurchaseItemsRequestDTO(item_dtos)
    purchase_topic = PurchasesTopic()
    purchase_items = PurchaseItems(purchase_topic)
    purchase_items(purchase_items_request_dto)
    return {
        "msg": "Item Purchase was accepted"
    }
