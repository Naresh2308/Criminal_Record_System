import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import matplotlib.pyplot as plt

# Database setup
conn = sqlite3.connect('criminaldb.db')
cursor = conn.cursor()

# Creating the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS criminals (
    criminal_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    year_caught INTEGER NOT NULL,
    crime_details TEXT NOT NULL,
    jail TEXT NOT NULL
)
''')
conn.commit()

# Functions
def insert_record():
    criminal_number = entry_criminal_number.get()
    name = entry_name.get()
    year_caught = entry_year_caught.get()
    crime_details = entry_crime_details.get()
    jail = entry_jail.get()

    if criminal_number and name and year_caught and crime_details and jail:
        try:
            cursor.execute('''
                INSERT INTO criminals (criminal_number, name, year_caught, crime_details, jail)
                VALUES (?, ?, ?, ?, ?)
            ''', (criminal_number, name, year_caught, crime_details, jail))
            conn.commit()
            messagebox.showinfo("Success", "Record inserted successfully!")
            clear_entries()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Criminal Number already exists!")
    else:
        messagebox.showerror("Error", "All fields are required!")

def search_record():
    criminal_number = entry_search_criminal_number.get()
    name = entry_search_name.get()

    if criminal_number:
        cursor.execute('SELECT * FROM criminals WHERE criminal_number=?', (criminal_number,))
    elif name:
        cursor.execute('SELECT * FROM criminals WHERE name=?', (name,))
    else:
        messagebox.showerror("Error", "Enter Criminal Number or Name to search!")
        return

    result = cursor.fetchone()

    if result:
        result_text.set(f"Criminal Found:\nNumber: {result[0]}\nName: {result[1]}\nYear Caught: {result[2]}\nCrime Details: {result[3]}\nJail: {result[4]}")
    else:
        result_text.set("Criminal not found.")

def delete_record():
    criminal_number = entry_delete_criminal_number.get()

    if criminal_number:
        cursor.execute('DELETE FROM criminals WHERE criminal_number=?', (criminal_number,))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Record deleted successfully!")
            entry_delete_criminal_number.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Criminal not found!")
    else:
        messagebox.showerror("Error", "Enter Criminal Number to delete!")

def show_pie_chart():
    cursor.execute('SELECT jail, COUNT(*) FROM criminals GROUP BY jail')
    data = cursor.fetchall()

    if data:
        jails = [row[0] for row in data]
        counts = [row[1] for row in data]

        plt.pie(counts, labels=jails, autopct='%1.1f%%')
        plt.title('Number of Cases per Jail')
        plt.show()
    else:
        messagebox.showerror("Error", "No data available to plot.")

# UI Setup
root = tk.Tk()
root.title("Criminal Database Management")

tab_control = ttk.Notebook(root)

# Insert Tab
tab_insert = ttk.Frame(tab_control)
tab_control.add(tab_insert, text='Insert Record')

label_criminal_number = ttk.Label(tab_insert, text="Criminal Number:")
label_criminal_number.grid(column=0, row=0, padx=10, pady=10)
entry_criminal_number = ttk.Entry(tab_insert)
entry_criminal_number.grid(column=1, row=0)

label_name = ttk.Label(tab_insert, text="Name:")
label_name.grid(column=0, row=1, padx=10, pady=10)
entry_name = ttk.Entry(tab_insert)
entry_name.grid(column=1, row=1)

label_year_caught = ttk.Label(tab_insert, text="Year Caught:")
label_year_caught.grid(column=0, row=2, padx=10, pady=10)
entry_year_caught = ttk.Entry(tab_insert)
entry_year_caught.grid(column=1, row=2)

label_crime_details = ttk.Label(tab_insert, text="Crime Details:")
label_crime_details.grid(column=0, row=3, padx=10, pady=10)
entry_crime_details = ttk.Entry(tab_insert)
entry_crime_details.grid(column=1, row=3)

label_jail = ttk.Label(tab_insert, text="Jail:")
label_jail.grid(column=0, row=4, padx=10, pady=10)
entry_jail = ttk.Entry(tab_insert)
entry_jail.grid(column=1, row=4)

button_insert = ttk.Button(tab_insert, text="Insert", command=insert_record)
button_insert.grid(column=1, row=5, padx=10, pady=10)

# Search Tab
tab_search = ttk.Frame(tab_control)
tab_control.add(tab_search, text='Search Record')

label_search_criminal_number = ttk.Label(tab_search, text="Criminal Number:")
label_search_criminal_number.grid(column=0, row=0, padx=10, pady=10)
entry_search_criminal_number = ttk.Entry(tab_search)
entry_search_criminal_number.grid(column=1, row=0)

label_search_name = ttk.Label(tab_search, text="Name:")
label_search_name.grid(column=0, row=1, padx=10, pady=10)
entry_search_name = ttk.Entry(tab_search)
entry_search_name.grid(column=1, row=1)

button_search = ttk.Button(tab_search, text="Search", command=search_record)
button_search.grid(column=1, row=2, padx=10, pady=10)

result_text = tk.StringVar()
label_result = ttk.Label(tab_search, textvariable=result_text, relief=tk.SUNKEN)
label_result.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Delete Tab
tab_delete = ttk.Frame(tab_control)
tab_control.add(tab_delete, text='Delete Record')

label_delete_criminal_number = ttk.Label(tab_delete, text="Criminal Number:")
label_delete_criminal_number.grid(column=0, row=0, padx=10, pady=10)
entry_delete_criminal_number = ttk.Entry(tab_delete)
entry_delete_criminal_number.grid(column=1, row=0)

button_delete = ttk.Button(tab_delete, text="Delete", command=delete_record)
button_delete.grid(column=1, row=1, padx=10, pady=10)

# Graph Tab
tab_graph = ttk.Frame(tab_control)
tab_control.add(tab_graph, text='Data Analysis')

button_pie_chart = ttk.Button(tab_graph, text="Show Pie Chart (Cases per Jail)", command=show_pie_chart)
button_pie_chart.grid(column=0, row=0, padx=10, pady=10)

tab_control.pack(expand=1, fill='both')

# Function to clear entries after insertion
def clear_entries():
    entry_criminal_number.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_year_caught.delete(0, tk.END)
    entry_crime_details.delete(0, tk.END)
    entry_jail.delete(0, tk.END)

root.mainloop()
