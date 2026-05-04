Feature: Product Management

Scenario: Read Product
  Given a product exists
  When I read the product
  Then I should see the product details

Scenario: Update Product
  Given a product exists
  When I update the product
  Then the product should be updated

Scenario: Delete Product
  Given a product exists
  When I delete the product
  Then the product should be removed

Scenario: List All Products
  Given multiple products exist
  When I list all products
  Then I should see all products

Scenario: Search by Name
  Given products exist
  When I search by name
  Then matching products are returned

Scenario: Search by Category
  Given products exist
  When I search by category
  Then matching products are returned

Scenario: Search by Availability
  Given products exist
  When I search by availability
  Then matching products are returned