from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent / "processed"

orders = pd.read_csv(folder / "ecommerce_sales_customer_analytics_150k.csv")
items = pd.read_csv(folder / "order_items.csv")
customers = pd.read_csv(folder / "customer_master.csv")
products = pd.read_csv(folder / "product_catalog.csv")

print("ROWS IN CLEANED FILES")
print("Orders:", len(orders))
print("Order items:", len(items))
print("Customers:", len(customers))
print("Products:", len(products))

print("\nDUPLICATE ID CHECK")
print("Order IDs:", orders["order_id"].duplicated().sum())
print("Customer IDs:", customers["customer_id"].duplicated().sum())
print("Product IDs:", products["product_id"].duplicated().sum())

print("\nTABLE CONNECTION CHECK")
print("Order items without an order:",
      (~items["order_id"].isin(orders["order_id"])).sum())
print("Order items without a product:",
      (~items["product_id"].isin(products["product_id"])).sum())
print("Orders without a customer:",
      (~orders["customer_id"].isin(customers["customer_id"])).sum())

print("\nCURRENCIES — KEEP THESE SEPARATE FOR NOW")
print(orders["currency"].value_counts())