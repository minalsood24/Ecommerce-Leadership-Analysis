# CommerceLeadership Dashboard

An e-commerce analytics project with Python data checks and cleaning, SQL analysis, and a Power BI report built as a PBIP project.

## Contents

- `01`–`06` Python scripts for data checks, cleaning, validation, and loading SQLite
- `sql/01_first_queries.sql` starter analysis queries
- `CommerceLeadership_Color_KPI_Dashboard/CommerceLeadership.pbip` Power BI project
- `dataset_statistics.csv` summary statistics

## Data and privacy

Customer-level source and processed CSV files, the SQLite database, and Power BI local cache files are intentionally not included in this public repository. The source files contain customer names, postal codes, reviews, and order-level details. Add only data you have permission to publish. Keep private or sensitive data out of GitHub.

To run the scripts with your own authorized data, place the source CSV files in the project root and processed CSV files in `processed/`. Install Python dependencies with `pip install -r requirements.txt`. The scripts resolve paths relative to their own location.

The Power BI model uses a `DataFolder` parameter. Set it to the local folder containing your authorized processed CSV files, then open `CommerceLeadership.pbip` in Power BI Desktop and refresh the model. The data folder is excluded from this public copy.

## Power BI pages

- Executive Overview
- Product Performance
- Customer Analysis
- Geography and Channel

## Requirements

- Python 3.10 or later
- pandas
- Power BI Desktop to open and refresh the report


