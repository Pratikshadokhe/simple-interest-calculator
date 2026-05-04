products = []

def read_product(product_id):
    return products[product_id]

def update_product(product_id, data):
    products[product_id].update(data)
    return products[product_id]

def delete_product(product_id):
    return products.pop(product_id)

def list_products(name=None, category=None, available=None):
    result = products

    if name:
        result = [p for p in result if p["name"] == name]

    if category:
        result = [p for p in result if p["category"] == category]

    if available is not None:
        result = [p for p in result if p["available"] == available]

    return result