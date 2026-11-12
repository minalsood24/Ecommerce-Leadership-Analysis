from pathlib import Path
import pandas as pd

folder = Path(__file__).resolve().parent
orders = pd.read_csv(folder / "ecommerce_sales_customer_analytics_150k.csv")

columns_to_check = [
    "return_status",
    "return_reason",
    "campaign_name",
    "coupon_code",
    "delivery_days",
    "estimated_delivery_days",
    "customer_rating",
    "customer_review",
    "review_sentiment",
]

# For each order status, show the percentage of blank values
missing_by_status = (
    orders.groupby("order_status")[columns_to_check]
    .apply(lambda group: group.isna().mean() * 100)
    .round(1)
)

print("PERCENT OF BLANK VALUES BY ORDER STATUS")
print(missing_by_status.to_string())

print("\nNUMBER OF ORDERS BY STATUS")
print(orders["order_status"].value_counts(dropna=False))

print("\nRETURN STATUS COUNTS")
print(orders["return_status"].value_counts(dropna=False))