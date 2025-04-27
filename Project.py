# OrderEase - Pizza Ordering System
# Developed by Jasmeen Kaur
# This application allows users to order pizza by selecting size, toppings, and entering delivery details.

import tkinter as tk
from tkinter import messagebox

# Function to go to Order Summary Window
def go_to_order_summary():
    selected_size = pizza_size.get()
    selected_toppings = [topping for topping, var in toppings_vars.items() if var.get()]

    if selected_size == "":
        messagebox.showerror("Input Error", "Please select a pizza size!")
        return
    if not selected_toppings:
        messagebox.showerror("Input Error", "Please select at least one topping!")
        return

    main_window.withdraw()  # Hide main window

    global summary_window
    summary_window = tk.Toplevel()
    summary_window.title("Order Summary")

    tk.Label(summary_window, text="Order Summary", font=("Arial", 16)).pack(pady=10)
    tk.Label(summary_window, text=f"Pizza Size: {selected_size}", font=("Arial", 12)).pack(pady=5)
    tk.Label(summary_window, text="Toppings: " + ", ".join(selected_toppings), font=("Arial", 12)).pack(pady=5)

    tk.Label(summary_window, text="Enter Name:", font=("Arial", 12)).pack(pady=5)
    global entry_name
    entry_name = tk.Entry(summary_window, width=30)
    entry_name.pack()

    tk.Label(summary_window, text="Enter Phone Number:", font=("Arial", 12)).pack(pady=5)
    global entry_phone
    entry_phone = tk.Entry(summary_window, width=30)
    entry_phone.pack()

    tk.Button(summary_window, text="Submit Order", command=submit_order).pack(pady=10)
    tk.Button(summary_window, text="Back", command=back_to_main).pack(pady=5)
    tk.Button(summary_window, text="Exit", command=summary_window.destroy).pack(pady=5)

# Function to submit order
def submit_order():
    name = entry_name.get()
    phone = entry_phone.get()
    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty!")
        return
    if not phone.isdigit():
        messagebox.showerror("Input Error", "Phone number must be numeric!")
        return
    messagebox.showinfo("Order Placed", "Thank you for your order!")
    main_window.destroy()

# Function to go back to main window
def back_to_main():
    summary_window.destroy()
    main_window.deiconify()

# Main GUI Window
main_window = tk.Tk()
main_window.title("OrderEase - Pizza Ordering System")
main_window.geometry("400x600")

tk.Label(main_window, text="Welcome to OrderEase Pizza Ordering", font=("Arial", 16)).pack(pady=10)

# Pizza Size Options
tk.Label(main_window, text="Select Pizza Size:", font=("Arial", 14)).pack(pady=10)
pizza_size = tk.StringVar(value="")
sizes = ["Small", "Medium", "Large"]
for size in sizes:
    tk.Radiobutton(main_window, text=size, variable=pizza_size, value=size).pack()

# Toppings Options
tk.Label(main_window, text="Select Toppings:", font=("Arial", 14)).pack(pady=10)
toppings_list = ["Cheese", "Pepperoni", "Mushrooms", "Olives"]
toppings_vars = {}
for topping in toppings_list:
    var = tk.BooleanVar()
    tk.Checkbutton(main_window, text=topping, variable=var).pack()
    toppings_vars[topping] = var

# Buttons
tk.Button(main_window, text="Next", command=go_to_order_summary).pack(pady=10)
tk.Button(main_window, text="Exit", command=main_window.destroy).pack(pady=5)

main_window.mainloop()