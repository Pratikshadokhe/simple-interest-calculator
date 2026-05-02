def test_get_product(client):
    response = client.get("/products/1")
    assert response.status_code == 200

def test_update_product(client):
    response = client.put("/products/1")
    assert response.status_code == 200

def test_delete_product(client):
    response = client.delete("/products/1")
    assert response.status_code == 204

def test_list_products(client):
    response = client.get("/products")
    assert response.status_code == 200

