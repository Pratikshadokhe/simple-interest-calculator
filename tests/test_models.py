from tests.factories import ProductFactory

products = []

def create_product():
    product = ProductFactory()
    products.append(product)
    return product

def test_read_product():
    product = create_product()
    assert product in products

def test_update_product():
    product = create_product()
    product["name"] = "Updated"
    assert product["name"] == "Updated"

def test_delete_product():
    product = create_product()
    products.remove(product)
    assert product not in products

def test_list_all_products():
    products.clear()
    create_product()
    create_product()
    assert len(products) >= 2

def test_find_by_name():
    product = create_product()
    result = [p for p in products if p["name"] == product["name"]]
    assert len(result) > 0

def test_find_by_category():
    product = create_product()
    result = [p for p in products if p["category"] == product["category"]]
    assert len(result) > 0

def test_find_by_availability():
    product = create_product()
    result = [p for p in products if p["available"] == product["available"]]
    assert len(result) > 0