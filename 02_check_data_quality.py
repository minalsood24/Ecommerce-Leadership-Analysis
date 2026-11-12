from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent

orders = pd.read_csv(folder / "ecommerce_sales_customer_analytics_150k.csv")
items = pd.read_csv(folder / "order_items.csv")
customers = pd.read_csv(folder / "customer_master.csv")
products = pd.read_csv(folder / "product_catalog.csv")

# 1. Check missing values in each table
tables = {
    "Orders": orders,
    "Order items": items,
    "Customers": customers,
    "Products": products,
}

for name, table in tables.items():
    print(f"\n{'=' * 60}")
    print(f"MISSING VALUES — {name}")
    print("=" * 60)
    missing = table.isna().sum()
    print(missing[missing > 0].sort_values(ascending=False))

# 2. Check whether the main IDs are duplicated
print("\nDUPLICATE ID CHECK")
print("Order IDs:", orders["order_id"].duplicated().sum())
print("Customer IDs:", customers["customer_id"].duplicated().sum())
print("Product IDs:", products["product_id"].duplicated().sum())

# 3. Check whether IDs in one table exist in the related table
print("\nTABLE CONNECTION CHECK")
print(
    "Order items without a matching order:",
    (~items["order_id"].isin(orders["order_id"])).sum()
)
print(
    "Order items without a matching product:",
    (~items["product_id"].isin(products["product_id"])).sum()
)
print(
    "Orders without a matching customer:",
    (~orders["customer_id"].isin(customers["customer_id"])).sum()
)

# 4. Check the currencies before adding up sales
print("\nCURRENCY COUNTS")
print(orders["currency"].value_counts(dropna=False))

# 5. Compare order and payment statuses
print("\nORDER STATUS BY PAYMENT STATUS")
print(pd.crosstab(orders["order_status"], orders["payment_status"], dropna=False))