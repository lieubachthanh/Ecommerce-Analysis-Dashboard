import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Insert into Categories
categories = [
    ('1', 'Electronics', 'Gadget', 'Top-selling items'),
    ('2', 'Clothing', 'Apparel', 'Seasonal discounts'),
    ('3', 'Home Appliances', 'Appliance', 'Latest models available'),
    ('4', 'Books', 'Education', 'Bestsellers list'),
    ('5', 'Beauty Products', 'Cosmetic', 'New arrivals'),
    ('6', 'Sports Equipment', 'Sport Gear', 'Popular among athletes'),
    ('7', 'Toys', 'Kids', 'Educational toys'),
    ('8', 'Furniture', 'Home Decor', 'Modern designs'),
    ('9', 'Groceries', 'Food & Beverages', 'Organic options'),
    ('10', 'Footwear', 'Shoes', 'Trending styles')
]
cursor.executemany('INSERT INTO Categories VALUES (?, ?, ?, ?)', categories)

# Insert into Products
products = [
    ('1001', '1', 'Smartphone', 699.99, 'Latest model'),
    ('1002', '2', 'T-shirt', 19.99, '100% cotton'),
    ('1003', '3', 'Washing Machine', 499.99, 'Energy efficient'),
    ('1004', '4', 'Fiction Novel', 14.99, 'Bestselling author'),
    ('1005', '5', 'Lipstick', 9.99, 'Long-lasting'),
    ('1006', '6', 'Soccer Ball', 29.99, 'FIFA approved'),
    ('1007', '7', 'Building Blocks', 39.99, 'Educational toy'),
    ('1008', '8', 'Sofa', 799.99, 'Modern design'),
    ('1009', '9', 'Organic Apples', 2.99, 'Fresh from farm'),
    ('1010', '10', 'Running Shoes', 89.99, 'Lightweight')
]
cursor.executemany('INSERT INTO Products VALUES (?, ?, ?, ?, ?)', products)

# Insert into Sellers
sellers = [
    ('101', '1001', 'ABC Electronics', 'Reliable vendor'),
    ('102', '1002', 'XYZ Clothing Co.', 'Top-rated supplier'),
    ('103', '1003', 'HomeAppliancePro', 'Fast delivery'),
    ('104', '1004', 'Book World', 'Diverse collection'),
    ('105', '1005', 'Beauty Haven', 'Premium products'),
    ('106', '1006', 'Sporty Gear', 'Quality assured'),
    ('107', '1007', 'ToyLand', 'Kid-friendly'),
    ('108', '1008', 'Decor Homes', 'Exclusive designs'),
    ('109', '1009', 'Fresh Grocers', 'Fresh produce'),
    ('110', '1010', 'FootStyle', 'Latest trends')
]
cursor.executemany('INSERT INTO Sellers VALUES (?, ?, ?, ?)', sellers)

# Insert into Customers
customers = [
    ('C001', 'John Doe', '123 Main St, City A', 'Frequent buyer'),
    ('C002', 'Jane Smith', '456 Elm St, City B', 'New customer'),
    ('C003', 'Bob Johnson', '789 Oak St, City C', 'Loyal customer'),
    ('C004', 'Alice Davis', '321 Pine St, City D', 'Prime member'),
    ('C005', 'Charlie Brown', '654 Maple St, City E', 'Gift card user'),
    ('C006', 'Dave Wilson', '987 Cedar St, City F', 'Referral program'),
    ('C007', 'Eve Martinez', '123 Birch St, City G', 'Newsletter subscriber'),
    ('C008', 'Frank Moore', '456 Spruce St, City H', 'Frequent buyer'),
    ('C009', 'Grace Lee', '789 Willow St, City I', 'VIP member'),
    ('C010', 'Henry Young', '321 Redwood St, City J', 'Discount code user')
]
cursor.executemany('INSERT INTO Customers VALUES (?, ?, ?, ?)', customers)

# Insert into ShoppingOrders
shopping_orders = [
    ('SO001', 'C001', '2024-01-10', 'Standard shipping'),
    ('SO002', 'C002', '2024-02-15', 'Expedited shipping'),
    ('SO003', 'C003', '2024-03-20', 'Standard shipping'),
    ('SO004', 'C004', '2024-04-25', 'Standard shipping'),
    ('SO005', 'C005', '2024-05-30', 'Expedited shipping'),
    ('SO006', 'C006', '2024-06-05', 'Standard shipping'),
    ('SO007', 'C007', '2024-07-10', 'Expedited shipping'),
    ('SO008', 'C008', '2024-08-15', 'Standard shipping'),
    ('SO009', 'C009', '2024-09-20', 'Expedited shipping'),
    ('SO010', 'C010', '2024-10-25', 'Standard shipping')
]
cursor.executemany('INSERT INTO ShoppingOrders VALUES (?, ?, ?, ?)', shopping_orders)

# Insert into Deliveries
deliveries = [
    ('D001', 'C001', '2024-01-12', 'On time'),
    ('D002', 'C002', '2024-02-17', 'Delayed'),
    ('D003', 'C003', '2024-03-22', 'On time'),
    ('D004', 'C004', '2024-04-27', 'On time'),
    ('D005', 'C005', '2024-06-01', 'Delayed'),
    ('D006', 'C006', '2024-06-07', 'On time'),
    ('D007', 'C007', '2024-07-12', 'On time'),
    ('D008', 'C008', '2024-08-17', 'Delayed'),
    ('D009', 'C009', '2024-09-22', 'On time'),
    ('D010', 'C010', '2024-10-27', 'On time')
]
cursor.executemany('INSERT INTO Deliveries VALUES (?, ?, ?, ?)', deliveries)

# Insert into Payments
payments = [
    ('P001', '1', '2024-01-01', 'Paid by credit card'),
    ('P002', '2', '2024-02-01', 'Paid by PayPal'),
    ('P003', '3', '2024-03-01', 'Paid by bank transfer'),
    ('P004', '4', '2024-04-01', 'Paid by debit card'),
    ('P005', '5', '2024-05-01', 'Paid by credit card'),
    ('P006', '6', '2024-06-01', 'Paid by PayPal'),
    ('P007', '7', '2024-07-01', 'Paid by bank transfer'),
    ('P008', '8', '2024-08-01', 'Paid by debit card'),
    ('P009', '9', '2024-09-01', 'Paid by credit card'),
    ('P010', '10', '2024-10-01', 'Paid by PayPal')
]
cursor.executemany('INSERT INTO Payments VALUES (?, ?, ?, ?)', payments)

# Insert into TransactionReports
transaction_reports = [
    ('R001', 'C001', 'SO001', '1001', 'P001', 'Successful'),
    ('R002', 'C002', 'SO002', '1002', 'P002', 'Successful'),
    ('R003', 'C003', 'SO003', '1003', 'P003', 'Successful'),
    ('R004', 'C004', 'SO004', '1004', 'P004', 'Successful'),
    ('R005', 'C005', 'SO005', '1005', 'P005', 'Successful'),
    ('R006', 'C006', 'SO006', '1006', 'P006', 'Successful'),
    ('R007', 'C007', 'SO007', '1007', 'P007', 'Successful'),
    ('R008', 'C008', 'SO008', '1008', 'P008', 'Successful'),
    ('R009', 'C009', 'SO009', '1009', 'P009', 'Successful'),
    ('R010', 'C010', 'SO010', '1010', 'P010', 'Successful')
]
cursor.executemany('INSERT INTO TransactionReports VALUES (?, ?, ?, ?, ?, ?)', transaction_reports)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database, tables, and data created successfully.")