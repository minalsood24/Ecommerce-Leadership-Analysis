from pathlib import Path
import pandas as pd

# Folder containing your original CSV files
source_folder = Path(__file__).resolve().parent

# New folder for the cleaned copies
output_folder = source_folder / "processed"
output_folder.mkdir(exist_ok=True)


def clean_table(file_name, id_columns, date_columns, numeric_columns):
    """Load one CSV, standardize its basic data types, and save a clean copy."""
    file_path = source_folder / file_name
    data = pd.read_csv(file_path)

    # Remove accidental spaces around text values.
    # Missing values remain missing; we are not filling them yet.
    text_columns = data.select_dtypes(include=["object", "str"]).columns
    for column in text_columns:
        data[column] = data[column].str.strip()

    # Keep IDs and postal codes as text.
    for column in id_columns:
        if column in data.columns:
            data[column] = data[column].astype("string").str.strip()

    # Convert dates to real date values.
    for column in date_columns:
        if column in data.columns:
            data[column] = pd.to_datetime(data[column], errors="coerce")

    # Convert numeric columns to numbers.
    for column in numeric_columns:
        if column in data.columns:
            data[column] = pd.to_numeric(data[column], errors="coerce")

    # Save a cleaned copy, keeping the original file unchanged.
    output_path = output_folder / file_name
    data.to_csv(output_path, index=False)

    print(f"\nCleaned: {file_name}")
    print("Rows and columns:", data.shape)
    print("Saved to:", output_path)
    print("Total missing values:", int(data.isna().sum().sum()))

    return data


# 1. Main order table
orders = clean_table(
    file_name="ecommerce_sales_customer_analytics_150k.csv",
    id_columns=["order_id", "customer_id", "customer_postal_code"],
    date_columns=["order_date"],
    numeric_columns=[
        "customer_age", "delivery_days", "estimated_delivery_days",
        "customer_rating", "loyalty_points_earned", "loyalty_points_redeemed",
        "quantity", "gross_sales", "discount_amount", "tax_amount",
        "shipping_cost", "net_sales", "product_cost", "profit",
        "profit_margin_percentage", "customer_lifetime_value",
        "customer_order_count",
    ],
)

# 2. Order item table
order_items = clean_table(
    file_name="order_items.csv",
    id_columns=["order_id", "product_id"],
    date_columns=[],
    numeric_columns=[
        "quantity", "unit_price", "discount_percentage", "discount_amount",
        "gross_sales", "tax_amount", "shipping_cost", "net_sales",
        "product_cost", "profit",
    ],
)

# 3. Customer table
customers = clean_table(
    file_name="customer_master.csv",
    id_columns=["customer_id", "customer_postal_code"],
    date_columns=[],
    numeric_columns=["customer_age", "customer_acquisition_cost"],
)

# 4. Product table
products = clean_table(
    file_name="product_catalog.csv",
    id_columns=["product_id"],
    date_columns=[],
    numeric_columns=["unit_price", "product_cost", "product_rating"],
)

print("\nCleaning step finished.")
print("Original files are still in:", source_folder)
print("Cleaned copies are in:", output_folder)