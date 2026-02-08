from models.product import Product
from models.customer import Customer
from models.order import Order
from repositories.inventory_repository import InventoryRepository
from utils.analytics_utils import calculate_total_revenue


class InventoryService:
