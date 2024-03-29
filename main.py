from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report, add_product_extra
from management.tab_handler import calculate_tab
from menu import products


def main():
    
    # res = get_product_by_id(25)
    # print(res)

    # print(get_products_by_type('drink'))

    # res = add_product(products,
    #                   description='Concept of healthy breakfast with mesli',
    #                   price=22.7, rating=2, title='Breakfast with muesli',
    #                   type='dairy')
    # print(res)

    # table_2 = [
    #     {"_id": 10, "amount": 3},
    #     {"_id": 20, "amount": 2},
    #     {"_id": 21, "amount": 5},
    # ]
    # print(calculate_tab(table_2))

    # print(menu_report())

    required_keys = ("description", "price", "rating", "title", "type")
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }
    res = add_product_extra(products, *required_keys, **new_product)
    print(res)


if __name__ == "__main__":
    main()
