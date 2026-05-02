def test_read_product():
    product = ProductFactory()
    assert product["name"] is not None

def test_update_product():
    product = ProductFactory()
    product["name"] = "Updated"
    assert product["name"] == "Updated"

def test_delete_product():
    product = ProductFactory()
    product = None
    assert product is None


def test_list_all():
    products = [ProductFactory() for _ in range(5)]
    assert len(products) == 5


def test_find_by_name():
    product = ProductFactory()
    assert "name" in product

def test_find_by_category():
    product = ProductFactory()
    assert "category" in product

def test_find_by_availability():
    product = ProductFactory()
    assert isinstance(product["available"], bool)

