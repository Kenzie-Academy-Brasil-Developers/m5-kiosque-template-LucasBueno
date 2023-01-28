from menu import products


def get_product_by_id(id: int):

    if not type(id) is int:
        raise TypeError('product id must be an int')

    for item in products:
        if item["_id"] == id:
            return item
    return {}


def get_products_by_type(types: str):
    result = []
    if not type(types) is str:
        raise TypeError('product type must be a str')
    for item in products:
        if item["type"] == types:
            result.append(item)
    return result if result else []


def add_product(menu, **product):
    if len(menu):
        max_id = max(item['_id'] for item in menu)
        product['_id'] = max_id + 1
        menu.append(product)
        return product
    product['_id'] = 1
    menu.append(product)
    return product


def menu_report():
    amount_products = len(products)
    price_average = 0
    most_common_type = {}
    for item in products:
        price_average += item["price"] / amount_products
        price_average = round(price_average, 2)
    types = [types["type"] for types in products]
    for item in types:
        most_common_type[(item)] = types.count(item)
    most_common_type = max(most_common_type, key=most_common_type.get)
    return f"Products Count: {amount_products} - Average Price: ${price_average} - Most Common Type: {most_common_type}"
