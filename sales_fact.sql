CREATE OR REPLACE TABLE `project_id.dataset_name.sales_fact` (
    invoice_id STRING,
    branch STRING,
    product_line STRING,
    quantity INT64,
    total FLOAT64,
    cogs FLOAT64,
    gross_income FLOAT64,
    rating FLOAT64,
    sale_date DATE
);
