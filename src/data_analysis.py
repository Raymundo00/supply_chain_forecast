"""
This script reads purchase order data from PostgreSQL
and performs basic aggregation to estimate lots per material.
"""

import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from src.db_connection import connect_to_db
from sqlalchemy.engine import Engine

# Load environment and get connection params
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def get_engine() -> Engine:
    """Create and return a SQLAlchemy engine using env vars."""
    url = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(url)

def load_orders() -> pd.DataFrame:
    """Load the orders table into a Pandas DataFrame."""
    engine = get_engine()
    query = "SELECT * FROM po_table.ordenes_compra;"
    df = pd.read_sql(query, engine)
    print("\nLoaded DataFrame:")
    print(df.head())
    return df

def aggregate_by_material(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by material and count number of orders (lots),
    and sum received quantity and demand estimate.
    """
    agg = (
        df.groupby("material")
          .agg(
            lots_received=("orden_compra", "count"),
            total_received=("cantidad_recibida", "sum"),
            total_demand=("demanda_estimacion", "sum")
          )
          .reset_index()
    )
    print("\nAggregation by material:")
    print(agg)
    return agg

if __name__ == "__main__":
    df_orders = load_orders()
    df_summary = aggregate_by_material(df_orders)
