CREATE DATABASE supply_chain;

USE supply_chain;

-- Check database
SELECT DATABASE();

-- Create suppliers table
CREATE TABLE suppliers (
    supplier_id VARCHAR(20),
    supplier_name VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50)
);

-- View table
SHOW TABLES;