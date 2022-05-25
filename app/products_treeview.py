from tkinter import *
from tkinter import ttk
import psycopg2
from config import config

def query_database():
    params = config()
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM product")
    records = cursor.fetchall()

    # Add the data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            treeview_products.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('evenrow',))
        else:
            treeview_products.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('oddrow',))
        # increment counter
        count += 1


    # Commit changes
    connection.commit()

    # Close our connection
    connection.close()

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
frame_treeview_products = ttk.Frame(products_container)
frame_treeview_products.grid(row=0, column=0, sticky='NSEW')

# Create a Treeview Scrollbar
#tree_scroll = Scrollbar(frame_treeview_products)
#tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
treeview_products = ttk.Treeview(frame_treeview_products, selectmode="extended")
treeview_products.grid(row=0, column=0, sticky='NSEW')

# Configure the Scrollbar
#tree_scroll.config(command=treeview_products.yview)

# Define Our Columns
treeview_products['columns'] = ("product_id", "name")

# Format Our Columns
treeview_products.column("#0", width=0, stretch=NO)
treeview_products.column("product_id", anchor=W, width=140)
treeview_products.column("name", anchor=W, width=140)


# Create Headings
treeview_products.heading("#0", text="", anchor=W)
treeview_products.heading("product_id", text="product_id", anchor=W)
treeview_products.heading("name", text="name", anchor=W)


# Create Striped Row Tags
treeview_products.tag_configure('oddrow', background="white")
treeview_products.tag_configure('evenrow', background="lightblue")


# Run to pull data from database on start
query_database()
