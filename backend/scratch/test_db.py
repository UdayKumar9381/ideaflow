import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Uday@123',
        database='ideaflow',
        port=3306
    )
    print("Successfully connected to MySQL!")
    conn.close()
except Exception as e:
    print(f"Failed to connect: {e}")
