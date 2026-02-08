from services.inventory_service import InventoryService
from views.inventory_view import InventoryView


class InventoryController:

    def __init__(self):
        self.service = InventoryService()
        self.view = InventoryView()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == "1":
                self.add_product_flow()
            elif choice == "2":
                self.add_customer_flow()
            elif choice == "3":
                self.place_order_flow()
            elif choice == "4":
                self.view_inventory_flow()
            elif choice == "5":
                self.view_orders_flow()
            elif choice == "6":
                self.analytics_flow()
            elif choice == "0":
                print("Exiting Inventory System...")
                break
            else:
                print("Invalid option.")

    def add_product_flow(self):
        data = self.view.get_product_input()
        self.service.add_product(data)

    def add_customer_flow(self):
        data = self.view.get_customer_input()
        self.service.add_customer(data)

    def place_order_flow(self):
        data = self.view.get_order_input()
        self.service.place_order(data)

    def view_inventory_flow(self):
        products = self.service.get_all_products()
        self.view.display_products(products)
