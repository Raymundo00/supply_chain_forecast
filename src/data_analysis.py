"""
This script reads purchase order data from PostgreSQL
and performs basic aggregation to estimate lots per material.
"""

import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from src.db_connection import connect_to_db


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

def load_po_data() -> pd.DataFrame:
    """
    Load purchase order data from po_table.po_data.

    Returns:
        pd.DataFrame: PO data including past and future entries
    """
    engine = get_engine()
    query = "SELECT * FROM po_table.po_data;"
    df = pd.read_sql(query, engine)
    print("\nPO data loaded:")
    print(df.head())
    return df

def summarize_historical_lots(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarizes historical performance per material.

    Parameters:
        df (pd.DataFrame): Full PO dataset

    Returns:
        pd.DataFrame: Aggregated summary with fulfillment and lots
    """
    historical = df[df["is_historical"] == True].copy()

    summary = (
        historical.groupby("material")
        .agg(
            total_pos=("po_number", "nunique"),
            total_quantity_ordered=("quantity_ordered", "sum"),
            total_quantity_received=("quantity_received", "sum"),
            lots_received=("lot_number", "nunique")
        )
        .reset_index()
    )

    summary["fulfillment_rate"] = (summary["total_quantity_received"] / summary["total_quantity_ordered"] * 100).round(2)

    print("\nHistorical summary:")
    print(summary)
    return summary


def estimate_future_lots(df: pd.DataFrame, historical_summary: pd.DataFrame) -> pd.DataFrame:
    """
    Estimate the number of lots we might receive for future POs based on historical fulfillment.

    Parameters:
        df (pd.DataFrame): Full PO dataset
        historical_summary (pd.DataFrame): Summary with lots and fulfillment

    Returns:
        pd.DataFrame: Estimated lots per material for future orders
    """
    future = df[df["is_historical"] == False].copy()

    # Merge with historical fulfillment rates and average quantity per lot
    merged = future.merge(historical_summary[["material", "fulfillment_rate", "lots_received", "total_quantity_received"]],
                          on="material", how="left")

    # Calculate avg quantity per lot
    merged["avg_qty_per_lot"] = merged["total_quantity_received"] / merged["lots_received"]
    merged["avg_qty_per_lot"] = merged["avg_qty_per_lot"].replace([np.inf, 0], np.nan)

    # Estimate lots: apply fulfillment rate and divide by typical lot size
    merged["expected_quantity"] = merged["quantity_ordered"] * (merged["fulfillment_rate"] / 100)
    merged["estimated_lots"] = (merged["expected_quantity"] / merged["avg_qty_per_lot"]).apply(np.ceil)

    print("\nFuture PO estimation:")
    print(merged[["material", "po_number", "quantity_ordered", "expected_quantity", "estimated_lots"]])

    return merged


if __name__ == "__main__":
    df = load_po_data()
    summary = summarize_historical_lots(df)
    estimates = estimate_future_lots(df, summary)
