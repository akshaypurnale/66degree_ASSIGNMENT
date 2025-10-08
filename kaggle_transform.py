from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

def run_query(query: str):
    """Helper function to run a SQL query"""
    job = client.query(query)
    job.result()  # Wait for the query to finish
    print("Query executed successfully.")

# Step 1: Create External Table from GCS
external_table_query = """
CREATE OR REPLACE EXTERNAL TABLE `project_id.dataset_name.supermarket_sales_raw`
OPTIONS (
  format = 'CSV',
  uris = ['gs://supermarket-sales-raw-data/raw/supermarket_sales.csv'],
  skip_leading_rows = 1
);
"""
run_query(external_table_query)

# Step 2: Transform Data into Dimension and Fact Tables
transform_queries = [
    """
    CREATE OR REPLACE TABLE `project_id.dataset_name.product_dim` AS
    SELECT DISTINCT
        Product_line AS product_line,
        Branch,
        City
    FROM `project_id.dataset_name.supermarket_sales_raw`;
    """,

    """
    CREATE OR REPLACE TABLE `project_id.dataset_name.store_dim` AS
    SELECT DISTINCT
        Branch,
        City,
        Customer_type,
        Gender
    FROM `project_id.dataset_name.supermarket_sales_raw`;
    """,

    """
    CREATE OR REPLACE TABLE `project_id.dataset_name.sales_fact` AS
    SELECT
        Invoice_ID,
        Branch,
        Product_line,
        Quantity,
        Total,
        cogs,
        gross_income,
        Rating,
        DATE(Date) AS sale_date
    FROM `project_id.dataset_name.supermarket_sales_raw`;
    """
]

for q in transform_queries:
    run_query(q)

print("Transformation completed and data loaded to BigQuery.")
