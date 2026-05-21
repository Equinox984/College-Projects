-- 1. Total spending per customer
SELECT
    c.first_name || ' ' || c.last_name AS customer_name,
    SUM(o.total_amount)                AS total_spent
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
GROUP BY o.customer_id;

-- 2. Most expensive product
SELECT name, price FROM Products
ORDER BY price DESC
LIMIT 1;

-- 3. Total sales
SELECT SUM(total_amount) AS total_sales FROM Orders;

-- 4. Most popular product
SELECT
    p.name,
    SUM(oi.quantity) AS units_sold
FROM Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY oi.product_id
ORDER BY units_sold DESC
LIMIT 1;

-- Thanks to our data, we know that Christian Roque is the customer who has spent the most money in the store ($338.99), 
-- the 24" monitor is the most expensive product ($249), 
-- and the USB-C Hub is the most popular product among customers. 
-- Finally, we know that all customers have spent a total of $559.96 in our store.
