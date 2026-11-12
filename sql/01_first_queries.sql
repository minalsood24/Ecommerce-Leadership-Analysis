-- 1. How many orders are in each status?
SELECT
    order_status,
    COUNT(*) AS order_count
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;


-- 2. How many completed, paid orders are there in each currency?
-- Keep currencies separate; adding USD, EUR, INR, and others together
-- would produce a misleading total.
SELECT
    currency,
    COUNT(*) AS paid_order_count,
    ROUND(SUM(net_sales), 2) AS net_sales_in_that_currency
FROM orders
WHERE order_status = 'Completed'
  AND payment_status = 'Paid'
GROUP BY currency
ORDER BY paid_order_count DESC;


-- 3. Which product categories have the most units sold?
SELECT
    p.product_category,
    SUM(i.quantity) AS units_sold,
    COUNT(DISTINCT i.order_id) AS orders_containing_category
FROM order_items AS i
JOIN products AS p
    ON i.product_id = p.product_id
JOIN orders AS o
    ON i.order_id = o.order_id
WHERE o.order_status = 'Completed'
  AND o.payment_status = 'Paid'
GROUP BY p.product_category
ORDER BY units_sold DESC;