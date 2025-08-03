# db.py
import psycopg2
import os
from dotenv import load_dotenv

# Manually load .env from 'database' folder
dotenv_path = os.path.join(os.path.dirname(__file__), 'database', '.env')
load_dotenv(dotenv_path)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
