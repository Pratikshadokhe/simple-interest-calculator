from faker import Faker
import random

fake = Faker()

def ProductFactory():
    return {
        "name": fake.word(),
        "category": fake.word(),
        "available": random.choice([True, False])
    }