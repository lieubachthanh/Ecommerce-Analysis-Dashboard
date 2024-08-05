from ecommerce import fetch_query

def total_revenue():
    query = '''
    SELECT SUM(Products.Price) FROM Products
    JOIN TransactionReports ON Products.ProductID = TransactionReports.ProductID
    '''
    result = fetch_query(query)
    return round(result[0][0],2) if result else 0

def category_sales():
    query = '''
    SELECT Categories.CategoryName, SUM(Products.Price) as TotalSales
    FROM Products
    JOIN Categories ON Products.CategoryID = Categories.CategoryID
    JOIN TransactionReports ON Products.ProductID = TransactionReports.ProductID
    GROUP BY Categories.CategoryName
    '''
    return fetch_query(query)

def customer_orders():
    query = '''
    SELECT Customers.CustomerName, COUNT(TransactionReports.OrderID) as NumberOfOrders
    FROM Customers
    JOIN TransactionReports ON Customers.CustomerID = TransactionReports.CustomerID
    GROUP BY Customers.CustomerName
    '''
    return fetch_query(query)

def products_sold():
    query = '''
    SELECT Products.ProductName, COUNT(TransactionReports.OrderID) as NumberOfOrders
    FROM Products
    JOIN TransactionReports ON Products.ProductID = TransactionReports.ProductID
    GROUP BY Products.ProductName
    '''
    return fetch_query(query)

def time_series_sales():
    query = '''
    SELECT strftime('%Y-%m', ShoppingOrders.DateOfOrder) as OrderMonth, SUM(Products.Price) as TotalSales
    FROM ShoppingOrders
    JOIN TransactionReports ON ShoppingOrders.OrderID = TransactionReports.OrderID
    JOIN Products ON TransactionReports.ProductID = Products.ProductID
    GROUP BY OrderMonth
    ORDER BY OrderMonth
    '''
    return fetch_query(query)

def main():
    print("Total Revenue: ", total_revenue())
    print("\nCategory Sales:")
    for row in category_sales():
        print(row)
    
    print("\nCustomer Orders:")
    for row in customer_orders():
        print(row)
    
    print("\nProducts Sold:")
    for row in products_sold():
        print(row)

    print("\nTime series sales:")
    for row in time_series_sales():
        print(row)
    

if __name__ == "__main__":
    main()
