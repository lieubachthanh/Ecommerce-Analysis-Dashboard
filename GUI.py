from ecommerce import create_database, execute_query, fetch_query
import tkinter as tk
from tkinter import messagebox, ttk

class EcommerceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-commerce Database Management")
        self.table_name = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Select Table:").grid(row=0, column=0, padx=10, pady=10)
        self.table_menu = ttk.Combobox(frame, textvariable=self.table_name, state='readonly')
        self.table_menu['values'] = ('Categories', 'Products', 'Sellers', 'Customers', 'ShoppingOrders', 'Deliveries', 'Payments', 'TransactionReports')
        self.table_menu.grid(row=0, column=1, padx=10, pady=10)
        self.table_menu.bind("<<ComboboxSelected>>", self.display_table)

        self.tree = ttk.Treeview(self.root, columns=(), show='headings')
        self.tree.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Add Record", command=self.add_record).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Edit Record", command=self.edit_record).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Delete Record", command=self.delete_record).grid(row=0, column=2, padx=10)

    def display_table(self, event=None):
        table = self.table_name.get()
        if not table:
            return
        
        columns = self.get_columns(table)
        self.tree.config(columns=columns)
        
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        rows = fetch_query(f"SELECT * FROM {table}")
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def get_columns(self, table):
        query = f"PRAGMA table_info({table})"
        columns_info = fetch_query(query)
        columns = [info[1] for info in columns_info]
        return columns

    def add_record(self):
        self.record_form("Add Record")

    def edit_record(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Edit Record", "Please select a record to edit.")
            return
        
        item = self.tree.item(selected_item[0])
        self.record_form("Edit Record", item['values'])

    def delete_record(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Delete Record", "Please select a record to delete.")
            return
        
        item = self.tree.item(selected_item[0])
        table = self.table_name.get()
        columns = self.get_columns(table)
        primary_key = columns[0]
        primary_key_value = item['values'][0]
        
        query = f"DELETE FROM {table} WHERE {primary_key} = ?"
        execute_query(query, (primary_key_value,))
        self.display_table()

    def record_form(self, title, record=None):
        form = tk.Toplevel(self.root)
        form.title(title)
        form.grab_set()
        
        table = self.table_name.get()
        columns = self.get_columns(table)
        
        entries = {}
        for i, col in enumerate(columns):
            tk.Label(form, text=col).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(form)
            entry.grid(row=i, column=1, padx=10, pady=5)
            if record:
                entry.insert(0, record[i])
            entries[col] = entry

        def save_record():
            data = {col: entry.get() for col, entry in entries.items()}
            if title == "Add Record":
                columns_str = ', '.join(data.keys())
                placeholders = ', '.join('?' * len(data))
                query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
                execute_query(query, tuple(data.values()))
            else:
                set_clause = ', '.join(f"{col} = ?" for col in data)
                primary_key = columns[0]
                primary_key_value = record[0]
                query = f"UPDATE {table} SET {set_clause} WHERE {primary_key} = ?"
                execute_query(query, tuple(data.values()) + (primary_key_value,))
            
            self.display_table()
            form.destroy()

        tk.Button(form, text="Save", command=save_record).grid(row=len(columns), column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    try:
        create_database()
    except:
        print('found ecommerce.db !')
    root = tk.Tk()
    app = EcommerceApp(root)
    root.mainloop()
