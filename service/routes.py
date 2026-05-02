@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    return {}, 200

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    return {}, 200

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    return {}, 204

@app.route("/products", methods=["GET"])
def list_products():
    return [], 200