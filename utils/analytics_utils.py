def calculate_total_revenue(orders):
    return sum(o["total_price"] for o in orders)
