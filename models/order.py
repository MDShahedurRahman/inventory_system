class Order:

    def __init__(self, order_id, customer_id, product_id, quantity, total_price):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price
        }
