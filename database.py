import os
import mysql.connector

db = mysql.connector.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    user=os.environ.get("DB_USER", "root"),
    password=os.environ.get("DB_PASSWORD", ""),
    database=os.environ.get("DB_NAME", "ktm_sales_management"),
    ssl_verify_identity=False
)

print("Database connected successfully!")

db.close()