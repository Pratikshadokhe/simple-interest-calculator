Scenario: Read a product
  Given a product exists
  When I read the product
  Then I should see the product

Scenario: Update a product
  Given a product exists
  When I update the product
  Then the product is updated

Scenario: Delete a product
  Given a product exists
  When I delete the product
  Then the product is removed

Scenario: List all products
  Given products exist
  When I list products
  Then I see all products

