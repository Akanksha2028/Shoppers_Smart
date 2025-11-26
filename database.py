import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Try to read DB_URI from environment (Render)
db_uri = os.getenv("DB_URI")

# If not set (or on Render where MySQL is not available), use SQLite file
if not db_uri:
    db_uri = "sqlite:///shopsmart.db"   # file-based DB inside project

app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
