class InventoryView:

    def show_menu(self):
        print("\n=== Inventory & Order System ===")
        print("1. Add Product")
        print("2. Add Customer")
        print("3. Place Order")
        print("4. View Inventory")
        print("5. View Orders")
        print("6. Sales Analytics")
        print("0. Exit")
        return input("Choose: ")

    def get_product_input(self):
        return {
            "name": input("Product name: "),
            "price": float(input("Price: ")),
            "stock": int(input("Stock quantity: "))
        }

    def get_customer_input(self):
        return {"name": input("Customer name: ")}

    def get_order_input(self):
        return {
            "customer_id": int(input("Customer ID: ")),
            "product_id": int(input("Product ID: ")),
            "quantity": int(input("Quantity: "))
        }
