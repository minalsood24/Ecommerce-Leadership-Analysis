from pathlib import Path
import sqlite3
import pandas as pd

folder = Path(__file__).resolve().parent
processed_folder = folder / "processed"
database_path = folder / "ecommerce_analysis.db"

tables = {
    "orders": "ecommerce_sales_customer_analytics_150k.csv",
    "order_items": "order_items.csv",
    "customers": "customer_master.csv",
    "products": "product_catalog.csv",
}

with sqlite3.connect(database_path) as connection:
    for table_name, file_name in tables.items():
        csv_path = processed_folder / file_name
        data = pd.read_csv(csv_path)

        # Store each CSV as a SQL table in the database.
        data.to_sql(table_name, connection, if_exists="replace", index=False)

        # Confirm how many rows were loaded.
        row_count = pd.read_sql_query(
            f"SELECT COUNT(*) AS row_count FROM {table_name}",
            connection,
        ).iloc[0]["row_count"]

        print(f"{table_name}: {row_count:,} rows loaded")

print(f"\nDatabase created at:\n{database_path}")