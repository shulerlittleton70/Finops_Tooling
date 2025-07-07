-- query_templates.sql

-- Monthly cost by service
SELECT
  product_code,
  SUM(blended_cost) AS total_cost
FROM {{ cur_table_name }}
WHERE year = {{ year }} AND month = {{ month }}
GROUP BY product_code
ORDER BY total_cost DESC;
