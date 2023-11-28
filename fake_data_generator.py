# fake_data_generator.py

import os
import django
from faker import Faker
from myapp.models import Category, Product

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

fake = Faker()

def generate_fake_data():
    # Generate fake categories
    categories = []
    for _ in range(5):
        category = Category(name=fake.word(), description=fake.text())
        category.save()
        categories.append(category)

    # Generate fake products
    for _ in range(20):
        product = Product(
            name=fake.word(),
            price=fake.random_number(digits=2),
            category=fake.random_element(categories),
        )
        product.save()

if __name__ == "__main__":
    generate_fake_data()
