from sqlalchemy import Column, Integer, String, Float
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Base  

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Float)
