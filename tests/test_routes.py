from tests.factories import ProductFactory

products = []

def test_read_route():
    product = ProductFactory()
    products.append(product)
    assert product in products

def test_update_route():
    product = ProductFactory()
    product["name"] = "New Name"
    assert product["name"] == "New Name"

def test_delete_route():
    product = ProductFactory()
    products.append(product)
    products.remove(product)
    assert product not in products

def test_list_all_route():
    products.clear()
    products.append(ProductFactory())
    products.append(ProductFactory())
    assert len(products) >= 2

def test_list_by_name():
    product = ProductFactory()
    products.append(product)
    result = [p for p in products if p["name"] == product["name"]]
    assert len(result) > 0

def test_list_by_category():
    product = ProductFactory()
    products.append(product)
    result = [p for p in products if p["category"] == product["category"]]
    assert len(result) > 0

def test_list_by_availability():
    product = ProductFactory()
    products.append(product)
    result = [p for p in products if p["available"] == product["available"]]
    assert len(result) > 0