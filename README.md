# 🛍️ ShopSmart – Location-Based Product Recommendation System

ShopSmart is a Flask-based backend system that provides location-based product recommendations by analyzing purchase trends of customers from the same area.  
It helps businesses improve product visibility, customer engagement, and sales.

## 🚀 Features
- Customer Login using customer ID
- Location-Based Recommendations
- Product Management (CRUD)
- Transaction Management (CRUD)
- CSV Importer for Customers, Products, Transactions
- RESTful API using Flask + SQLAlchemy
- Postman Tested Endpoints

## 🛠️ Tech Stack
- Backend: Flask, Python  
- Database: SQLAlchemy   
- Data Processing: Pandas  
- API Testing: Postman  
- Version Control: Git, GitHub  
## 📂 Project Structure
```
ShoppersSmart/
│── main.py 
│── database.py
│── csv_importer.py 
│── recommender_utils.py
│── requirements.txt
│── README.md
│
├── models/
│   ├── customer.py
│   ├── product.py
│   └── transaction.py
│
├── routes/
│   ├── customer_routes.py
│   ├── product_routes.py
│   ├── transaction_routes.py
│   └── recommendation_routes.py
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── transactions.csv
```

## 🧑‍💼 Customer APIs

**POST** `/customers`  
**GET** `/customers`  
**GET** `/customers/<id>`  
**PUT** `/customers/<id>`  
**DELETE** `/customers/<id>`  


## 📦 Product APIs

**POST** `/products`  
**GET** `/products`  
**GET** `/products/<id>`  
**PUT** `/products/<id>`  
**DELETE** `/products/<id>`  


## 💳 Transaction APIs

**POST** `/transactions`  
**GET** `/transactions`  
**GET** `/transactions/<id>`  
**PUT** `/transactions/<id>`  
**DELETE** `/transactions/<id>`  


## 🎯 Recommendation API

**POST** `/recommend`

📌 **Example Request:**

```json
{
  "customer_id": 253
}
