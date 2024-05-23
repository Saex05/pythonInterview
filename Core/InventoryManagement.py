from pprint import pprint


def order_inventory(products_list, sort_key="name", reverse=True):
    return sorted(products_list, key=lambda x: x[sort_key], reverse=reverse)


# Example Input:
products = [
{"name": "Product A", "price": 100, "stock": 5},
{"name": "Product B", "price": 200, "stock": 3},
{"name": "Product C", "price": 50, "stock": 10}
]
sort_key = "price"
reverse = True


sorted_products = order_inventory(products, sort_key, reverse)
pprint(sorted_products)
