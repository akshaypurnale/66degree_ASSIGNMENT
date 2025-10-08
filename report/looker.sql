SELECT 
  s.branch,
  p.product_line, 
  SUM(s.total) AS total_sales, 
  ROUND(AVG(s.rating), 2) AS avg_rating, 
  RANK() OVER (PARTITION BY s.branch ORDER BY SUM(s.total) DESC) AS product_rank, 
  AVG(SUM(s.total)) OVER (ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7d_sales 
  FROM project_id.dataset_name.sales_fact s 3 
  JOIN project_id.dataset_name.product_dim p 
  ON s.product_line = p.product_line 
  GROUP BY s.branch, p.product_line, s.sale_date;
