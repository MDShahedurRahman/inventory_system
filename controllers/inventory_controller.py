from services.inventory_service import InventoryService
from views.inventory_view import InventoryView


class InventoryController:

    def __init__(self):
        self.service = InventoryService()
        self.view = InventoryView()
