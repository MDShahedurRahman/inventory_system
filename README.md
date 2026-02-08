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
