# Smart-Inventory-Order-Manager
The Smart Inventory Management System is a lightweight yet powerful web-based application built with Python Flask for managing products, orders, and inventory levels.
It allows small businesses to track stock in real time, manage customer orders, and automatically generate PDF invoices — all through a clean and easy-to-use dashboard.


🚀 Features
✅ Product Management – Add, edit, and delete products with name, description, price, and stock quantity.
✅ Order Management – Create customer orders with multiple products and quantities.
✅ Stock Tracking – Automatic stock deduction upon order creation.
✅ Low Stock Alerts – Quickly see which products are running low.
✅ PDF Invoice Generation – Automatically generate a professional invoice for each order.
✅ Simple & Lightweight – Runs locally or on any server with minimal setup.
✅ Cross-Platform – Works on Windows, macOS, and Linux.

🛠️ Technology Stack
Backend: Python, Flask

Frontend: HTML, CSS (via Jinja2 templates)

Database: SQLite (default, can be changed to MySQL/PostgreSQL)

PDF Generation: ReportLab

Forms & Validation: Flask-WTF

ORM: Flask-SQLAlchemy

smart_inventory/
│
├── app.py                  # Main application file
├── models.py               # Database models
├── forms.py                # Web forms for products & orders
├── utils.py                # Helper functions (PDF generation, etc.)
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── product_form.html
│   ├── order_form.html
│
├── static/                 # Static assets (CSS, JS, images)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


⚙️ Installation & Setup
git clone https://github.com/yourusername/smart_inventory.git
cd smart_inventory

2️⃣ Create Virtual Environment
python -m venv venv
.\venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser
http://

📑 Usage Guide
Add Products
Go to Add Product

Fill in product details (name, description, price, quantity)

Save to add it to the inventory

Place an Order
Go to New Order

Select products and enter quantities

Enter customer details

Click submit to:

Deduct stock from inventory

Generate PDF invoice

Manage Stock
View all products on the home page

Edit or delete products

Low stock items are highlighted for quick restocking

🖨️ Invoice Generation
Each order generates a PDF invoice with:

Company name (editable in app.py or utils.py)

Customer details

Order summary with prices and quantities

Total amount

🛡️ Requirements
Python 3.8+

Flask 2.2+

Flask-WTF 1.1+

Flask-SQLAlchemy 3.0+

ReportLab 4.0+





📌 Future Enhancements
User authentication & roles

Barcode scanner integration

Email invoice directly to customer

Multi-warehouse stock tracking

Export reports to Excel/CSV


📜 License
This project is open-source and free to use for personal or commercial purposes.


