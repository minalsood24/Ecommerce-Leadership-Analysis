# E-Commerce Leadership Analysis

An end-to-end e-commerce analytics project that combines Python data-quality checks and cleaning, SQL analysis, SQLite storage, and a Power BI leadership dashboard. The workflow turns related order, customer, product, and order-item files into a validated dataset for business performance analysis.

## Project goals

- Inspect source files and identify data-quality issues, missing values, and key relationships.
- Create cleaned copies while preserving the original files.
- Load the cleaned tables into SQLite for repeatable SQL analysis.
- Present leadership-focused measures and trends in Power BI.

## Dashboard

The Power BI report contains four pages:

- **Executive Overview** — headline sales, profit, discount, and customer measures.
- **Product Performance** — product-level sales and profitability analysis.
- **Customer Analysis** — customer trends and behavior.
- **Geography and Channel** — performance across locations and sales channels.

The model keeps currencies separate where needed; monetary values should not be added across currencies without conversion.

## Workflow and scripts

Run the scripts from the repository root, in this order:

| Step | File | Purpose |
|---|---|---|
| 1 | `01 Data Check.py` | Reviews file shapes, columns, and sample records. It also expects `dataset_statistics.csv`. |
| 2 | `02_check_data_quality.py` | Checks missing values, duplicate IDs, table relationships, currency values, and order/payment statuses. |
| 3 | `03_investigate_missing_values.py` | Examines missingness in the source data. |
| 4 | `04_clean_data.py` | Trims text and standardizes selected values and types; writes cleaned copies to `processed/`. Source files remain unchanged. |
| 5 | `05_validate_clean_data.py` | Checks row counts and key relationships in the cleaned files. |
| 6 | `06_load_sqlite.py` | Loads the cleaned tables into `ecommerce_analysis.db` as `orders`, `order_items`, `customers`, and `products`. |
| 7 | `sql/01_first_queries.sql` | Provides starter SQL analysis queries for the SQLite tables. |

The scripts use paths relative to their location, so the project can be placed in a different folder without changing a personal computer path.

## Repository contents

- `01`–`06` Python scripts for inspection, quality checks, cleaning, validation, and SQLite loading.
- `sql/01_first_queries.sql` starter queries.
- `requirements.txt` Python dependency list.
- `CommerceLeadership_Color_KPI_Dashboard/` Power BI Project (`.pbip`) report and semantic model.

## Dataset and privacy

The CSV files and generated SQLite database are **not included** in this public repository. The source data contains customer-level fields such as names, postal codes, reviews, and order details. Publishing those records could expose personal or sensitive information, and the original dataset’s redistribution terms have not been confirmed. The Power BI local cache and user-specific settings are also excluded because they can contain embedded data or local configuration.

The dataset’s original download URL was not available when this README was prepared. Before obtaining or redistributing the data, confirm the source and its license or terms of use. Do not commit customer or confidential data to a public repository.

To reproduce the analysis, obtain the same source files from a source you are authorized to use and place them in the repository root:

- `customer_master.csv`
- `dataset_statistics.csv`
- `ecommerce_sales_customer_analytics_150k.csv`
- `order_items.csv`
- `product_catalog.csv`

The scripts create `processed/` and the SQLite database locally. These generated data files are excluded by `.gitignore` and should remain local unless you have explicit permission to publish them.

## Getting started

### Requirements

- Python 3.10 or later
- Power BI Desktop to open and refresh the report

### Python and SQLite workflow

1. Install Python dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

2. Put the authorized source CSV files listed above in the repository root.
3. Run the numbered Python scripts in order. For example:

   ```bash
   python "01 Data Check.py"
   python 02_check_data_quality.py
   python 03_investigate_missing_values.py
   python 04_clean_data.py
   python 05_validate_clean_data.py
   python 06_load_sqlite.py
   ```

4. Open `ecommerce_analysis.db` with a SQLite client and run the queries in `sql/01_first_queries.sql`.

### Power BI

1. Run the cleaning step so the `processed/` folder contains the four cleaned data tables.
2. Open `CommerceLeadership_Color_KPI_Dashboard/CommerceLeadership.pbip` in Power BI Desktop.
3. Set the model’s `DataFolder` parameter to the full local path of the `processed/` folder.
4. Refresh the model.

The report definition is included, but the data is not; the report will need authorized local CSV files before it can refresh.

## Notes

This repository contains project code and report definitions, not a licensed copy of the dataset. Results may differ if a different dataset or a different version is used. Confirm that the currencies, column names, and table relationships match before comparing results.
