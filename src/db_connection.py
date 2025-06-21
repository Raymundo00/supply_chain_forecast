"""
This script connects to the PostgreSQL database using environment variables.
"""

import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection as PGConnection

# Load environment variables from .env file
load_dotenv()

# Read variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def connect_to_db() -> PGConnection | None:
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        print("✅ Connection to PostgreSQL successful.")
        return connection
    except Exception as e:
        print("❌ Error connecting to PostgreSQL:", e)
        return None
