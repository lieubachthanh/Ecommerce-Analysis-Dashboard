import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from analysis import total_revenue, category_sales, customer_orders, products_sold, time_series_sales

class AnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Ecommerce Analysis Dashboard")
        self.geometry("900x700")

        self.create_widgets()

    def create_widgets(self):
        notebook = ttk.Notebook(self)
        notebook.pack(pady=10, expand=True)

        frame1 = ttk.Frame(notebook, width=900, height=700)
        frame2 = ttk.Frame(notebook, width=900, height=700)
        frame3 = ttk.Frame(notebook, width=900, height=700)
        frame4 = ttk.Frame(notebook, width=900, height=700)
        frame5 = ttk.Frame(notebook, width=900, height=700)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)
        frame3.pack(fill='both', expand=True)
        frame4.pack(fill='both', expand=True)
        frame5.pack(fill='both', expand=True)

        notebook.add(frame1, text='Total Revenue')
        notebook.add(frame2, text='Category Sales')
        notebook.add(frame3, text='Customer Orders')
        notebook.add(frame4, text='Products Sold')
        notebook.add(frame5, text='Time Series Sales')

        self.display_total_revenue(frame1)
        self.display_category_sales(frame2)
        self.display_customer_orders(frame3)
        self.display_products_sold(frame4)
        self.display_time_series_sales(frame5)

    def display_total_revenue(self, frame):
        revenue = total_revenue()
        label = ttk.Label(frame, text=f"Total Revenue: ${revenue:.2f}", font=("Helvetica", 16))
        label.pack(pady=20)

    def display_category_sales(self, frame):
        data = category_sales()
        categories, sales = zip(*data)
        
        figure = plt.Figure(figsize=(7, 5), dpi=100)
        ax = figure.add_subplot(111)
        ax.pie(sales, labels=categories, autopct='%1.1f%%', startangle=140)
        ax.set_title('Category Sales')

        chart = FigureCanvasTkAgg(figure, frame)
        chart.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def display_customer_orders(self, frame):
        data = customer_orders()
        customers, orders = zip(*data)

        figure = plt.Figure(figsize=(7, 5), dpi=100)
        ax = figure.add_subplot(111)
        bars = ax.bar(customers, orders)
        ax.set_title('Customer Orders')
        ax.set_xlabel('Customer')
        ax.set_ylabel('Number of Orders')

        # Rotate x-axis labels
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

        figure.tight_layout()  # Adjust layout to fit labels

        chart = FigureCanvasTkAgg(figure, frame)
        chart.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def display_products_sold(self, frame):
        data = products_sold()
        products, sold = zip(*data)

        figure = plt.Figure(figsize=(7, 5), dpi=100)
        ax = figure.add_subplot(111)
        bars = ax.bar(products, sold)
        ax.set_title('Products Sold')
        ax.set_xlabel('Product')
        ax.set_ylabel('Number of Orders')

        # Rotate x-axis labels
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

        figure.tight_layout()  # Adjust layout to fit labels

        chart = FigureCanvasTkAgg(figure, frame)
        chart.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def display_time_series_sales(self, frame):
        data = time_series_sales()
        months, sales = zip(*data)

        figure = plt.Figure(figsize=(7, 5), dpi=100)
        ax = figure.add_subplot(111)
        ax.plot(months, sales, marker='o', linestyle='-')
        ax.set_title('Time Series Sales')
        ax.set_ylabel('Total Sales')

        # Rotate x-axis labels
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

        figure.tight_layout()  # Adjust layout to fit labels

        chart = FigureCanvasTkAgg(figure, frame)
        chart.get_tk_widget().pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = AnalysisApp()
    app.mainloop()
