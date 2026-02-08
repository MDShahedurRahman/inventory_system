from models.product import Product
from models.customer import Customer
from models.order import Order
from repositories.inventory_repository import InventoryRepository
from utils.analytics_utils import calculate_total_revenue


class InventoryService:

    def __init__(self):
        self.repo = InventoryRepository()


def add_product(self, product_data):
    data = self.repo.load_data()
    new_id = len(data["products"]) + 1

    product = Product(new_id,
                      product_data["name"],
                      product_data["price"],
                      product_data["stock"])

    data["products"].append(product.to_dict())
    self.repo.save_data(data)


def add_customer(self, customer_data):
    data = self.repo.load_data()
    new_id = len(data["customers"]) + 1

    customer = Customer(new_id, customer_data["name"])
    data["customers"].append(customer.to_dict())
    self.repo.save_data(data)
