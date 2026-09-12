CREATE DATABASE ecommerce_sales;

USE ecommerce_sales;

CREATE TABLE ecommerce_products (
    Product VARCHAR(50),
    Product_Brand VARCHAR(50),
    Item_Category VARCHAR(255),
    Subcategory_1 VARCHAR(255),
    Subcategory_2 VARCHAR(255),
    Item_Rating DECIMAL(2,1),
    Date DATE,
    Selling_Price DECIMAL(12,2),
    Year INT,
    Month_Number INT,
    Month_Name VARCHAR(20),
    Year_Month_Value VARCHAR(10),
    Quarter_Number INT
);
SHOW TABLES;

SELECT COUNT(*) AS Total_Rows
FROM ecommerce_products;

SELECT COUNT(*) AS Total_Products
FROM ecommerce_products;

SELECT 
    ROUND(AVG(Selling_Price), 2) AS Average_Selling_Price
FROM ecommerce_products;

SELECT
    MIN(Selling_Price) AS Minimum_Price,
    MAX(Selling_Price) AS Maximum_Price
FROM ecommerce_products;

SELECT
    Item_Category,
    COUNT(*) AS Product_Count
FROM ecommerce_products
GROUP BY Item_Category
ORDER BY Product_Count DESC
LIMIT 10;

SELECT
    Product_Brand,
    COUNT(*) AS Product_Count
FROM ecommerce_products
GROUP BY Product_Brand
ORDER BY Product_Count DESC
LIMIT 10;

SELECT
    Year,
    COUNT(*) AS Product_Count,
    ROUND(AVG(Selling_Price), 2) AS Average_Price,
    ROUND(AVG(Item_Rating), 2) AS Average_Rating
FROM ecommerce_products
GROUP BY Year
ORDER BY Year;

SELECT
    Item_Category,
    COUNT(*) AS Product_Count,
    ROUND(AVG(Selling_Price), 2) AS Average_Price,
    ROUND(AVG(Item_Rating), 2) AS Average_Rating
FROM ecommerce_products
GROUP BY Item_Category
ORDER BY Product_Count DESC
LIMIT 10;

SELECT
    CASE
        WHEN Selling_Price <= 500 THEN '₹0-₹500'
        WHEN Selling_Price <= 1000 THEN '₹501-₹1,000'
        WHEN Selling_Price <= 5000 THEN '₹1,001-₹5,000'
        WHEN Selling_Price <= 10000 THEN '₹5,001-₹10,000'
        ELSE 'Above ₹10,000'
    END AS Price_Range,
    COUNT(*) AS Product_Count,
    ROUND(AVG(Selling_Price), 2) AS Average_Price,
    ROUND(AVG(Item_Rating), 2) AS Average_Rating
FROM ecommerce_products
GROUP BY Price_Range
ORDER BY MIN(Selling_Price);

SELECT
    Item_Rating,
    COUNT(*) AS Product_Count,
    ROUND(AVG(Selling_Price), 2) AS Average_Price
FROM ecommerce_products
GROUP BY Item_Rating
ORDER BY Item_Rating DESC;

SELECT
    Product,
    Product_Brand,
    Item_Category,
    Item_Rating,
    Selling_Price
FROM ecommerce_products
ORDER BY Selling_Price DESC
LIMIT 10;

SELECT
    Item_Category,
    COUNT(*) AS Product_Count,
    ROUND(AVG(Selling_Price), 2) AS Average_Price
FROM ecommerce_products
GROUP BY Item_Category
HAVING COUNT(*) >= 10
ORDER BY Average_Price DESC
LIMIT 10;

SELECT
    Item_Category,
    COUNT(*) AS Product_Count,
    ROUND(AVG(Item_Rating), 2) AS Average_Rating,
    ROUND(AVG(Selling_Price), 2) AS Average_Price
FROM ecommerce_products
GROUP BY Item_Category
HAVING COUNT(*) >= 10
ORDER BY Average_Rating DESC
LIMIT 10;





