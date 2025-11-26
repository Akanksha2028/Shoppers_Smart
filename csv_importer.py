import pandas as pd
from database import db, engine
from models.customer import Customer
from models.product import Product
from models.transaction import Transaction

def import_customers(csv_path='data/customers.csv'):
    df = pd.read_csv(csv_path)
    df.to_sql(Customer.__tablename__, con=engine, if_exists='append', index=False)
    print(f"✅ Imported {len(df)} customers")

def import_products(csv_path='data/Products.csv'):
    df = pd.read_csv(csv_path)
    df.to_sql(Product.__tablename__, con=engine, if_exists='append', index=False)
    print(f"✅ Imported {len(df)} products")


def import_transactions(csv_path='data/Transactions.csv'):
    df = pd.read_csv(csv_path)
    df.to_sql(Transaction.__tablename__, con=engine, if_exists='append', index=False)
    print(f"✅ Imported {len(df)} transactions")

if __name__ == "__main__":
    import_customers()
    import_products()
    import_transactions()
