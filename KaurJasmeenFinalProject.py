# OrderEase - Pizza Ordering System
# Developed by Jasmeen Kaur
# This application allows users to order pizza by selecting size, toppings, and entering delivery details.

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # You must install pillow library for images: pip install pillow

# Global variables to store user choices
pizza_size = None
toppings_vars = {}
entry_name = None
entry_address = None
entry_phone = None
main_window = None
summary_window = None


# Function to validate user input
def validate_inputs():
    if not entry_name.get():
        messagebox.showerror("Input Error", "Name cannot be empty.")
        return False
    if not entry_address.get():
        messagebox.showerror("Input Error", "Address cannot be empty.")
        return False
    if not entry_phone.get().isdigit():
        messagebox.showerror("Input Error", "Phone number must be numeric.")
        return False
    return True


# Function to submit order
def submit_order():
    if validate_inputs():
        messagebox.showinfo("Order Submitted", "Thank you for your order!")
        summary_window.destroy()
        main_window.destroy()


# Function to go back to main window
def back_to_main():
    summary_window.destroy()
    main_window.deiconify()


# Function to go to Order Summary window
def go_to_order_summary():
    selected_size = pizza_size.get()
    selected_toppings = [topping for topping, var in toppings_vars.items() if var.get()]

    if selected_size == "":
        messagebox.showerror("Input Error", "Please select a pizza size!")
        return
    if not selected_toppings:
        messagebox.showerror("Input Error", "Please select at least one topping!")
        return

    # Hide Main Window
    main_window.withdraw()

    # Create Order Summary Window
    global summary_window
    summary_window = tk.Toplevel()
    summary_window.title("Order Summary")
    summary_window.geometry("400x500")

    # Labels for Order Summary
    tk.Label(summary_window, text="Order Summary", font=("Arial", 16)).pack(pady=10)
    tk.Label(summary_window, text=f"Pizza Size: {selected_size}", font=("Arial", 12)).pack(pady=5)
    tk.Label(summary_window, text="Toppings: " + ", ".join(selected_toppings), font=("Arial", 12)).pack(pady=5)

    # Entry fields for customer info
    tk.Label(summary_window, text="Name:", font=("Arial", 12)).pack(pady=5)
    global entry_name
    entry_name = tk.Entry(summary_window, width=30)
    entry_name.pack()

    tk.Label(summary_window, text="Address:", font=("Arial", 12)).pack(pady=5)
    global entry_address
    entry_address = tk.Entry(summary_window, width=30)
    entry_address.pack()

    tk.Label(summary_window, text="Phone Number:", font=("Arial", 12)).pack(pady=5)
    global entry_phone
    entry_phone = tk.Entry(summary_window, width=30)
    entry_phone.pack()

    # Buttons
    tk.Button(summary_window, text="Submit Order", command=submit_order).pack(pady=10)
    tk.Button(summary_window, text="Back", command=back_to_main).pack(pady=5)
    tk.Button(summary_window, text="Exit", command=summary_window.destroy).pack(pady=5)


# Main Window (Home Page)
def create_main_window():
    global main_window
    main_window = tk.Tk()
    main_window.title("OrderEase - Pizza Ordering System")
    main_window.geometry("500x600")

    tk.Label(main_window, text="Welcome to OrderEase Pizza Ordering", font=("Arial", 16)).pack(pady=10)

    # Pizza Image (first image)
    pizza_img = Image.open("pizza1.png")  # Make sure you have pizza1.png in same folder
    pizza_img = pizza_img.resize((200, 150))
    pizza_photo = ImageTk.PhotoImage(pizza_img)
    tk.Label(main_window, image=pizza_photo).pack(pady=5)
    main_window.pizza_photo = pizza_photo  # To prevent image garbage collection

    # Pizza Size Selection
    tk.Label(main_window, text="Select Pizza Size:", font=("Arial", 14)).pack(pady=10)
    global pizza_size
    pizza_size = tk.StringVar(value="")

    sizes = ["Small", "Medium", "Large"]
    for size in sizes:
        tk.Radiobutton(main_window, text=size, variable=pizza_size, value=size).pack()

    # Toppings Selection
    tk.Label(main_window, text="Select Toppings:", font=("Arial", 14)).pack(pady=10)
    toppings_list = ["Cheese", "Pepperoni", "Mushrooms", "Olives", "Onions", "Tomatoes"]
    global toppings_vars
    toppings_vars = {}
    for topping in toppings_list:
        var = tk.BooleanVar()
        tk.Checkbutton(main_window, text=topping, variable=var).pack()
        toppings_vars[topping] = var

    # Second Pizza Image (second image)
    pizza2_img = Image.open("pizza2.png")  # Make sure you have pizza2.png
    pizza2_img = pizza2_img.resize((200, 150))
    pizza2_photo = ImageTk.PhotoImage(pizza2_img)
    tk.Label(main_window, image=pizza2_photo).pack(pady=5)
    main_window.pizza2_photo = pizza2_photo

    # Buttons
    tk.Button(main_window, text="Next", command=go_to_order_summary).pack(pady=10)
    tk.Button(main_window, text="Exit", command=main_window.destroy).pack(pady=5)

    main_window.mainloop()


# Run the program
create_main_window()
  
