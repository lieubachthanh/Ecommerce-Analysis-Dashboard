# Ecommerce-Analysis-Dashboard
This project is designed to analyze and visualize data from an eCommerce database. It provides functionalities for creating and populating the database, inserting new data, performing data analysis, and visualizing the results through a graphical user interface (GUI).

## Project Structure
```
Ecommerce-Analysis-Dashboard/
    │
    ├── ecommerce.py
    ├── analysis.py
    ├── insert.py
    ├── GUI.py
    ├── DA_UI.py
    └── requirements.txt
```


### Files Description

- **ecommerce.py**: Contains code to create and populate the database with initial data.
- **analysis.py**: Contains code to analyze the data in the database.
- **insert.py**: Contains code to insert new data into the database.
- **GUI.py**: Provides an interface to view tables in the database, and perform add, delete, and edit operations.
- **DA_UI.py**: Provides an interface to visualize the analyzed data.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/lieubachthanh/Ecommerce-Analysis-Dashboard.git
    cd Ecommerce-Analysis-Dashboard
    ```

2. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Initialize the Database**:
    Run the script to create and populate the database.
    ```bash
    python ecommerce.py
    ```

## Usage

### Inserting Data

To insert new data into the database, use:
```bash
python insert.py
```

###  Viewing and Modifying Data
To view tables and perform add, delete, and edit operations, run:

```bash
python GUI.py
```

###  Analyzing and Visualizing Data:
To analyze and visualize the data, run:

```bash
python DA_UI.py
```

## Details
### database.py
Contains the SQL schema and initial data to populate the following tables:
- Categories
- Products
- Sellers
- Customers
- ShoppingOrders
- Deliveries
- Payments
- TransactionReports

### database.py

Provides functions to perform various data analysis operations:

- *total_revenue()*: Calculates total revenue.
- *category_sales()*: Analyzes sales by category.
- *customer_orders()*: Analyzes orders by customers.
- *products_sold()*: Analyzes the number of products sold.
- *time_series_sales()*: Analyzes sales over time.

###  insert.py
Contains functions to insert new data into the database. This can be expanded to handle user input or batch data insertions.

###  GUI.py
Provides a simple Tkinter GUI to:

- View tables in the database.
- Add new records.
- Delete records.
- Edit existing records.

###  DA_UI.py
Provides a Tkinter GUI to visualize analyzed data:

- Displays total revenue.
- Shows category sales in a pie chart.
- Displays customer orders in a bar chart.
- Shows products sold in a bar chart.
- Visualizes time series sales in a line chart

## Requirements
The required Python packages are listed in requirements.txt and can be installed using:
```bash
pip install -r requirements.txt
```

##  Contact
For any inquiries, please contact [lieubachthanh2002@gmail.com].