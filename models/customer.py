class Customer:

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name
        }
