from faker import Faker
import random

fake = Faker()

def ProductFactory():
    return {
        "name": fake.word(),
        "description": fake.sentence(),
        "price": round(random.uniform(10.0, 100.0), 2),
        "category": random.choice(["Electronics", "Clothing", "Food"]),
        "available": random.choice([True, False])
    }