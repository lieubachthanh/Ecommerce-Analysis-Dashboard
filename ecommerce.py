import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create tables
def create_database():
    cursor.execute('''
    CREATE TABLE Categories (
        CategoryID TEXT PRIMARY KEY,
        CategoryName TEXT NOT NULL,
        CategoryType TEXT,
        AdditionalInfo TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE Products (
        ProductID TEXT PRIMARY KEY,
        CategoryID TEXT,
        ProductName TEXT NOT NULL,
        Price REAL NOT NULL,
        AdditionalInfo TEXT,
        FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Sellers (
        SellerID TEXT PRIMARY KEY,
        ProductID TEXT,
        SupplierName TEXT NOT NULL,
        AdditionalInfo TEXT,
        FOREIGN KEY (ProductID) REFERENCES Products (ProductID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Customers (
        CustomerID TEXT PRIMARY KEY,
        CustomerName TEXT NOT NULL,
        ContactAddress TEXT,
        AdditionalInfo TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE ShoppingOrders (
        OrderID TEXT PRIMARY KEY,
        CustomerID TEXT,
        DateOfOrder TEXT NOT NULL,
        AdditionalInfo TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Deliveries (
        DeliveryID TEXT PRIMARY KEY,
        CustomerID TEXT,
        DateOfDelivery TEXT NOT NULL,
        AdditionalInfo TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE Payments (
        PaymentID TEXT PRIMARY KEY,
        CategoryID TEXT,
        Date TEXT NOT NULL,
        AdditionalInfo TEXT,
        FOREIGN KEY (CategoryID) REFERENCES Categories (CategoryID)
    )
    ''')

    cursor.execute('''
    CREATE TABLE TransactionReports (
        ReportID TEXT PRIMARY KEY,
        CustomerID TEXT,
        OrderID TEXT,
        ProductID TEXT,
        PaymentID TEXT,
        AdditionalInfo TEXT,
        FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID),
        FOREIGN KEY (OrderID) REFERENCES ShoppingOrders (OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products (ProductID),
        FOREIGN KEY (PaymentID) REFERENCES Payments (PaymentID)
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database and tables created successfully.")


def execute_query(query, parameters=()):
    with sqlite3.connect('ecommerce.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()

def fetch_query(query, parameters=()):
    with sqlite3.connect('ecommerce.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchall()