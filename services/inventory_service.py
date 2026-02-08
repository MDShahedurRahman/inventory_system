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


def place_order(self, order_data):
    data = self.repo.load_data()
    new_id = len(data["orders"]) + 1

    product = next(
        (p for p in data["products"]
         if p["product_id"] == order_data["product_id"]),
        None
    )

    if not product:
        print("Product not found.")
        return

    if product["stock"] < order_data["quantity"]:
        print("Not enough stock available.")
        return

    total_price = product["price"] * order_data["quantity"]
    product["stock"] -= order_data["quantity"]

    order = Order(new_id,
                  order_data["customer_id"],
                  order_data["product_id"],
                  order_data["quantity"],
                  total_price)

    data["orders"].append(order.to_dict())
    self.repo.save_data(data)


def get_all_products(self):
    return self.repo.load_data()["products"]
