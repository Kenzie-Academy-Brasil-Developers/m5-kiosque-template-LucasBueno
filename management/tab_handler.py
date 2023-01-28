from menu import products
from .product_handler import get_product_by_id


def calculate_tab(consumptions):
    subtotal = 0
    for item in consumptions:
        product = get_product_by_id(item["_id"])
        subtotal += product["price"] * item["amount"]
    subtotal = str(round(subtotal, 2))
    return {"subtotal": f'${subtotal}'}