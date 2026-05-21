-- 1. All customers
SELECT * FROM Customers;

-- 2. All products
SELECT * FROM Products;

-- 3. Orders with customer name and product name
SELECT
    o.order_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    -- || is like + in Python, used to concatenate strings.
    -- In this case: "Christian" + " " + "Roque"
    p.name AS product_name,
    oi.quantity,
    o.order_date,
    o.total_amount
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id;

-- 4. Products above a certain price ($50)
SELECT * FROM Products
WHERE price > 50;

-- 5. All orders for one specific customer (Christian Roque, customer_id = 1)
SELECT
    o.order_id,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    o.total_amount
FROM Orders o
JOIN Order_Items oi ON o.order_id = oi.order_id
JOIN Products p ON oi.product_id = p.product_id
WHERE o.customer_id = 1;
