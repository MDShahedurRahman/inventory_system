# Advanced Python MVC Project  
## Inventory & Order Management System (CLI)

A modular **Inventory & Order Management System** built using **Python** and the **MVC (Model–View–Controller)** architecture.

This project simulates a real-world backend system like a mini e-commerce platform, where you can manage products, customers, orders, stock updates, and sales analytics using a command-line interface.

It is designed as a **portfolio-quality project** to demonstrate clean architecture, layered design, and commit-by-method development.

---

## 🚀 Features

- Add and manage products in inventory  
- Track product stock levels  
- Register customers  
- Place customer orders  
- Automatically reduce stock after orders  
- Prevent out-of-stock purchases  
- View full inventory list  
- View complete order history  
- Sales and revenue analytics report  
- Persistent JSON-based storage  
- Clean MVC separation  

---

## 🏗 Project Architecture (MVC)

```
inventory_system/
│
├── main.py
│
├── controllers/
│   └── inventory_controller.py
│
├── models/
│   ├── product.py
│   ├── customer.py
│   └── order.py
│
├── services/
│   └── inventory_service.py
│
├── repositories/
│   └── inventory_repository.py
│
├── views/
│   └── inventory_view.py
│
├── utils/
│   ├── validation_utils.py
│   └── analytics_utils.py
│
└── data/
    └── inventory_data.json
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher

---

### Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/inventory-order-system.git
cd inventory-order-system
```

Run the application:

```bash
python main.py
```

---

## ▶️ Usage

When you run the program, you will see a menu:

```
1. Add Product
2. Add Customer
3. Place Order
4. View Inventory
5. View Orders
6. Sales Analytics
0. Exit
```

---

## 📌 Example Workflow

1. Add products such as Laptop, Phone, Headphones  
2. Register customers  
3. Place an order for a customer  
4. Stock is automatically reduced  
5. View inventory updates  
6. Generate sales analytics report  

---

## 💾 Data Storage

All inventory, customer, and order data is stored in:

```
data/inventory_data.json
```

This ensures persistence across program runs.

---

## 📊 Sales Analytics

The system provides business-level insights such as:

- Total number of products
- Total orders placed
- Total revenue generated

Example report:

```
=== Sales Report ===
total_products: 5
total_orders: 3
total_revenue: 1200.00
```

---

## 🧠 Concepts Demonstrated

- MVC Architecture in Python  
- Clean Code and Modular Design  
- Repository Pattern  
- Business Logic Layer (Service Layer)  
- JSON Persistence  
- Inventory Stock Management  
- Order Processing Workflow  
- Backend Analytics Reporting  
- Git Commit Discipline  

---

## 📝 Git Commit Strategy (50 Commits)

This project is designed to be built with **one method per commit**, like a real software workflow.

### Phase 1: Setup (1–10)

- main.py → main()
- inventory_controller.py → run()
- inventory_view.py → show_menu()
- inventory_repository.py → load_data(), save_data()
- product.py, customer.py, order.py base models

---

### Phase 2: Model Methods (11–18)

- Product.reduce_stock()
- Serialization methods (to_dict, from_dict)
- Analytics utility methods
- Validation helpers

---

### Phase 3: Service Layer Core (19–35)

- add_product()
- add_customer()
- place_order()
- generate_sales_report()
- Restock product feature
- Delete/update product methods
- Low stock alerts
- Revenue breakdown enhancements

---

### Phase 4: Controller Flows (36–45)

- add_product_flow()
- add_customer_flow()
- place_order_flow()
- view_inventory_flow()
- analytics_flow()
- Input validation and error handling

---

### Phase 5: View & UI Improvements (46–50)

- Improved formatted printing
- Better menu experience
- Report display improvements
- Final README + cleanup

---

## 🧪 Testing Suggestions

- Add multiple products and verify stock updates  
- Place orders until stock runs out  
- Restart the program to confirm persistence  
- Verify revenue analytics accuracy  
- Test invalid inputs (wrong product/customer IDs)

---

## 📌 Future Enhancements

- Replace JSON with SQLite/PostgreSQL  
- Add product categories  
- Add order cancellation/refund support  
- Implement REST API using FastAPI  
- Add admin vs customer roles  
- Export reports to CSV  

---

## 📄 .gitignore (Recommended)

```
__pycache__/
*.pyc
.env
.idea/
.vscode/
data/inventory_data.json
```

---

## 👨‍💻 Author

**Md Shahedur Rahman**  
Master’s in Computer Science  
Data Engineering | Backend Development | Python | Java | Distributed Systems  

---

✅ Portfolio-ready project demonstrating backend architecture and real-world order processing logic.
