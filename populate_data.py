import os
import django
import random
from faker import Faker  # Import the Faker library for generating random names

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'D_Hack.settings')
django.setup()

from main.models import Seller, Item, Customer, Order
from main.models import User  # Import User model if you're using it

fake = Faker()  # Initialize the Faker object

def create_customer(seller):
    name = fake.name()  # Generate a random name
    address = f'Address {random.randint(1, 100)}'
    phone_num = f'Phone {random.randint(100000, 999999)}'

    customer = Customer.objects.create(
        seller=seller,
        name=name,
        address=address,
        phone_num=phone_num
    )
    return customer

def create_item(seller):
    title = f'Item {random.randint(1, 100)}'  # Generate a random word as the item title
    available_units = random.randint(1, 100)

    item = Item.objects.create(
        seller=seller,
        title=title,
        available_units=available_units
    )
    return item

def create_order(seller, customer, item):
    price = round(random.uniform(10, 100), 2)  # Random price between 10 and 100
    quantity = random.randint(1, 5)  # Random quantity between 1 and 5

    order = Order.objects.create(
        seller=seller,
        customer=customer,
        item=item,
        price=price,
        quantity=quantity
    )
    return order

if __name__ == '__main__':
    # Replace 'your_seller_username' with the seller's username you want to associate with the data.
    seller = User.objects.get(username='SahityaSingh').seller

    for _ in range(50):  # Populate with 50 data points
        customer = create_customer(seller)
        item = create_item(seller)
        order = create_order(seller, customer, item)
        print(f'Data point created for seller {seller.user.username}: customer={customer.name}, item={item.title}, order={order}')
