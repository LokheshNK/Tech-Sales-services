import tkinter as tk
from tkinter import ttk, messagebox

item_details = {
    "Mobiles": {
        "Iphone 15": 99999,
        "Samsung S24 Ultra": 125000,
        "OnePlus nord 4": 73999,
        "Redmi Note 14 ": 33999,
        "Google pixel 7a": 27199,
        "Realme note 16": 21999,
        "LG": 899
    },
    "Laptop": {
        "macbook pro m3": 299999,
        "Dell Galvanic": 78999,
        "HP Pavillion": 72999,
        "Lenovo ideapad": 63999,
        "Asus TUF F15": 79999,
        "Acer Nitro 5": 64999
    },
    "TV": {
        "Samsung OLED": 120000,
        "Sony Bravia": 300000,
        "LG WebOS": 40000,
        "Sony Xperia": 78999,
        "Hisense KODAK": 32999,
        "Panasonic OLED": 22222
    },
    "AC": {
        "Carrier": 32000,
        "Daikin": 11939,
        "LG": 31099,
        "Mitsubishi Electric": 12499,
        "Panasonic": 59299,
        "Samsung": 15199,
        "Whirlpool": 11099
    },
    "Fan": {
        "Havells": 9229,
        "Bajaj": 679,
        "Usha": 1289,
        "Orient": 1469,
        "Crompton": 1179,
        "Oscar": 3359,
        "Luminous": 55109
    },
    "Fridge": {
        "Samsung": 11099,
        "LG": 33999,
        "Whirlpool": 51199,
        "Haier": 22899,
        "Godrej": 331099,
        "Panasonic": 22999,
        "Bosch": 11299
    },
    "Heater": {
        "Havells": 11199,
        "Bajaj": 33179,
        "Usha": 22159,
        "Orient": 33139,
        "Crompton": 2189,
        "Oscar": 55169,
        "Morphy Richards": 33219
    }
}

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.configure(bg="#FFFFFF")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()


        self.root.geometry("300x200+{}+{}".format(int((screen_width - 300) / 2), int((screen_height - 200) / 2)))

        self.user_credentials_file = "user_credentials.txt"
        self.logged_in_username = None

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = ttk.Button(self.root, text="Login", command=self.check_login, width=20)
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open(self.user_credentials_file, "r") as file:
                user_data = file.readlines()
        except FileNotFoundError:
            with open(self.user_credentials_file, "w"):
                pass
            user_data = []

        for line in user_data:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                messagebox.showinfo("Login Successful", "Welcome back!")
                self.logged_in_username = username
                self.root.destroy()  # Close the login window
                root = tk.Tk()
                app = TechSalesAndServicesGUI(root, self.logged_in_username)
                root.mainloop()
                return

        create_new_user = messagebox.askyesno("User Not Found", "Username not found. Would you like to create a new account?")
        if create_new_user:
            with open(self.user_credentials_file, "a") as file:
                file.write(f"{username},{password}\n")
            messagebox.showinfo("Account Created", "New account created successfully. Please login again.")
        else:
            messagebox.showinfo("Cancelled", "Operation cancelled. Please try again.")

class TechSalesAndServicesGUI:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Tech Sales and Services")
        self.root.configure(bg="#FFFFFF")  # Set background color to white

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Set window size and position to fullscreen
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.purchase_history_file = "purchase_history.txt"
        self.user_info_file = "user_info.txt"
        self.logged_in_username = username

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = ttk.Label(self.root, text="Tech Sales and Services", font=("Helvetica", 24))
        self.title_label.pack(pady=(40, 20))


        user_info_exists = False
        try:
            with open(self.user_info_file, "r") as file:
                for line in file:
                    if line.startswith(f"Username: {self.logged_in_username}"):
                        user_info_exists = True
                        name = line.split(",")[1].strip().split(":")[1].strip()
                        age = line.split(",")[2].strip().split(":")[1].strip()
                        customer_number = line.split(",")[3].strip().split(":")[1].strip()
                        break
        except FileNotFoundError:
            pass

        if user_info_exists:

            self.name_label = ttk.Label(self.root, text="Name:", font=("Helvetica", 16))
            self.name_label.pack()
            self.name_entry = ttk.Entry(self.root, font=("Helvetica", 14))
            self.name_entry.insert(0, name)
            self.name_entry.pack(pady=5)

            self.age_label = ttk.Label(self.root, text="Age:", font=("Helvetica", 16))
            self.age_label.pack(pady=5)
            self.age_entry = ttk.Entry(self.root, font=("Helvetica", 14))
            self.age_entry.insert(0, age)
            self.age_entry.pack(pady=5)

            self.customer_number_label = ttk.Label(self.root, text="Customer Number:", font=("Helvetica", 16))
            self.customer_number_label.pack(pady=5)
            self.customer_number_entry = ttk.Entry(self.root, font=("Helvetica", 14))
            self.customer_number_entry.insert(0, customer_number)
            self.customer_number_entry.pack(pady=5)

        else:

            self.name_label = ttk.Label(self.root, text="Name:", font=("Helvetica", 16))
            self.name_label.pack()
            self.name_entry = ttk.Entry(self.root, font=("Helvetica", 14))
            self.name_entry.pack(pady=5)

            self.age_label = ttk.Label(self.root, text="Age:", font=("Helvetica", 16))
            self.age_label.pack(pady=5)
            self.age_entry = ttk.Entry(self.root, font=("Helvetica", 14))
            self.age_entry.pack(pady=5)

            self.customer_number_label = ttk.Label(self.root, text="Customer Number:", font=("Helvetica", 16))
            self.customer_number_label.pack(pady=5)
            self.customer_number_entry = ttk.Entry(self.root, font=("Helvetica", 14))
            self.customer_number_entry.pack(pady=5)


        save_button = ttk.Button(self.root, text="Save", command=self.save_user_info, width=30)
        save_button.pack(pady=20)

        # Buy New Item Button
        buy_new_item_button = ttk.Button(self.root, text="Buy New Item", command=self.open_buy_new_item_window, width=30)
        buy_new_item_button.pack(pady=20)

        # Services Button
        services_button = ttk.Button(self.root, text="Services", command=self.open_services_window, width=30)
        services_button.pack(pady=20)

        # Purchase History Button
        history_button = ttk.Button(self.root, text="Purchase History", command=self.show_purchase_history, width=30)
        history_button.pack(pady=20)

        # Return a Product Button
        return_product_button = ttk.Button(self.root, text="Return a Product", command=self.return_product, width=30)
        return_product_button.pack(pady=20)

        # Logout Button
        logout_button = ttk.Button(self.root, text="Logout", command=self.logout, width=30)
        logout_button.pack(pady=20)

        # Exit Button
        exit_button = ttk.Button(self.root, text="Exit", command=self.exit_program, width=30)
        exit_button.pack(pady=20)

        # Increase font size of buttons
        for widget in (save_button, buy_new_item_button, services_button, history_button, return_product_button, logout_button, exit_button):
            widget.configure(font=("Helvetica", 16))

    def save_user_info(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        customer_number = self.customer_number_entry.get()

        # Check if all fields are filled
        if name and age and customer_number:
            # Save user info to a file
            with open(self.user_info_file, "a") as file:
                file.write(f"Username: {self.logged_in_username}, Name: {name}, Age: {age}, Customer Number: {customer_number}\n")
            messagebox.showinfo("Saved", "User information saved successfully.")
        else:
            messagebox.showwarning("Incomplete Information", "Please fill in all fields.")

    def open_buy_new_item_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Buy New Item")
        new_window.geometry("800x600")  # Set a larger size for the window

        # Initialize BuyNewItemApp in the new window
        app = BuyNewItemApp(new_window, self.logged_in_username)

    def open_services_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Services")
        new_window.geometry("800x600")  # Set a larger size for the window

        # Initialize ServicesApp in the new window
        app = ServicesApp(new_window, self.logged_in_username)

    def show_purchase_history(self):
        if self.logged_in_username:
            try:
                with open("purchase_history.txt", "r") as file:
                    purchase_history = file.readlines()
                user_purchase_history = [purchase.strip() for purchase in purchase_history if purchase.startswith(self.logged_in_username)]
                if user_purchase_history:
                    # Create a new window to display purchase history
                    history_window = tk.Toplevel(self.root)
                    history_window.title("Purchase History")
                    history_window.geometry("600x400")

                    # Create a text widget to display the purchase history
                    purchase_history_text = tk.Text(history_window, wrap=tk.WORD)
                    purchase_history_text.pack(fill=tk.BOTH, expand=True)

                    # Insert the purchase history into the text widget
                    for purchase in user_purchase_history:
                        purchase_history_text.insert(tk.END, f"{purchase}\n")
                    
                    # Disable editing in the text widget
                    purchase_history_text.config(state=tk.DISABLED)
                else:
                    messagebox.showinfo("Purchase History", "No purchase history found for this user.")
            except FileNotFoundError:
                messagebox.showinfo("Purchase History", "No purchase history found.")
        else:
            messagebox.showwarning("Warning", "No user logged in.")

    def return_product(self):
        if self.logged_in_username:
            try:
                with open("purchase_history.txt", "r") as file:
                    purchase_history = file.readlines()
                user_purchase_history = [purchase.strip() for purchase in purchase_history if purchase.startswith(self.logged_in_username)]
                if user_purchase_history:
                    # Create a new window to display the products the user has bought
                    return_product_window = tk.Toplevel(self.root)
                    return_product_window.title("Return a Product")
                    return_product_window.geometry("600x400")

                    # Create a listbox to display the user's purchased products
                    product_listbox = tk.Listbox(return_product_window, selectmode=tk.SINGLE, font=("Helvetica", 12))
                    product_listbox.pack(fill=tk.BOTH, expand=True)

                    # Insert the user's purchased products into the listbox
                    for purchase in user_purchase_history:
                        product_listbox.insert(tk.END, purchase)

                    # Function to handle the return process
                    def return_selected_product():
                        selected_index = product_listbox.curselection()
                        if selected_index:
                            selected_item = product_listbox.get(selected_index)
                            # Extract the product name and price from the selected item
                            product_name = selected_item.split(":")[1].split("from")[0].strip()
                            product_category = selected_item.split("from")[1].strip().split("for")[0].strip()
                            product_price = selected_item.split("for")[1].strip().split("Rs.")[1].strip()
                            # Remove the selected item from the purchase history file
                            with open("purchase_history.txt", "r+") as file:
                                lines = file.readlines()
                                file.seek(0)
                                for line in lines:
                                    if line.strip() != selected_item:
                                        file.write(line)
                                file.truncate()
                            # Show a message indicating the product has been returned and refunded
                            messagebox.showinfo("Product Returned", f"{product_name} from {product_category} has been returned and Rs.{product_price} refunded to your account.")
                            # Close the window after returning the product
                            return_product_window.destroy()
                        else:
                            messagebox.showwarning("No Selection", "Please select a product to return.")

                    # Button to return the selected product
                    return_button = ttk.Button(return_product_window, text="Return Product", command=return_selected_product)
                    return_button.pack(pady=10)
                else:
                    messagebox.showinfo("No Purchased Products", "You have not purchased any products yet.")
            except FileNotFoundError:
                messagebox.showinfo("Purchase History", "No purchase history found.")
        else:
            messagebox.showwarning("Warning", "No user logged in.")

    def logout(self):
        self.root.destroy()
        root = tk.Tk()
        login = LoginWindow(root)
        root.mainloop()

    def exit_program(self):
        self.root.destroy()

class BuyNewItemApp:
    def __init__(self, root, username):
        self.root = root
        self.root.configure(bg="#FFFFFF")  # Set background color to white

        self.username = username
        self.cart = []  # Initialize an empty cart to store selected items

        self.create_widgets()

    def create_widgets(self):
        # Create a combobox to select item category
        self.category_label = ttk.Label(self.root, text="Select Category:", font=("Helvetica", 16))
        self.category_label.pack(pady=10)
        self.category_combobox = ttk.Combobox(self.root, values=list(item_details.keys()), font=("Helvetica", 14))
        self.category_combobox.pack(pady=5)

        # Create a combobox to select item
        self.item_label = ttk.Label(self.root, text="Select Item:", font=("Helvetica", 16))
        self.item_label.pack(pady=10)
        self.item_combobox = ttk.Combobox(self.root, state="disabled", font=("Helvetica", 14))
        self.item_combobox.pack(pady=5)

        # Cart Button
        cart_button = ttk.Button(self.root, text="Add to Cart", command=self.add_to_cart, width=30)
        cart_button.pack(pady=10)

        # Buy Button
        buy_button = ttk.Button(self.root, text="Buy", command=self.buy_items, width=30)
        buy_button.pack(pady=10)

        # Cart Listbox
        self.cart_label = ttk.Label(self.root, text="Cart", font=("Helvetica", 16))
        self.cart_label.pack(pady=10)
        self.cart_listbox = tk.Listbox(self.root, font=("Helvetica", 12))
        self.cart_listbox.pack(fill=tk.BOTH, expand=True)

        # Button to remove item from cart
        remove_button = ttk.Button(self.root, text="Remove from Cart", command=self.remove_from_cart, width=30)
        remove_button.pack(pady=10)

        # Bind the item selection combobox to update options based on category selection
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_item_combobox)

    def update_item_combobox(self, event):
        selected_category = self.category_combobox.get()
        if selected_category:
            items = list(item_details[selected_category].keys())
            self.item_combobox.config(values=items, state="readonly")

    def add_to_cart(self):
        selected_item = self.item_combobox.get()
        if selected_item:
            self.cart.append(selected_item)  # Add selected item to the cart list
            self.cart_listbox.insert(tk.END, selected_item)  # Display selected item in the cart listbox
        else:
            messagebox.showwarning("Incomplete Selection", "Please select an item to add to cart.")

    def remove_from_cart(self):
        selected_index = self.cart_listbox.curselection()
        if selected_index:
            del self.cart[selected_index[0]]  # Remove selected item from the cart list
            self.cart_listbox.delete(selected_index[0])  # Remove selected item from the cart listbox
        else:
            messagebox.showwarning("No Selection", "Please select an item to remove from cart.")

    def buy_items(self):
        if self.cart:
            total_price = 0
            # Calculate the total price of all items in the cart
            for item in self.cart:
                category = None
                for cat, items in item_details.items():
                    if item in items:
                        category = cat
                        total_price += item_details[cat][item]
                        break
            # Write the purchase to the purchase history file
            with open("purchase_history.txt", "a") as file:
                for item in self.cart:
                    file.write(f"{self.username}: Purchased {item} from {category} for Rs.{item_details[category][item]}\n")
            messagebox.showinfo("Purchase Complete", f"Items purchased successfully for total amount Rs.{total_price}.")
            self.root.destroy()
        else:
            messagebox.showwarning("Empty Cart", "Please add items to the cart before buying.")


class ServicesApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Services")
        self.root.configure(bg="#FFFFFF")  # Set background color to white

        self.username = username
        self.selected_items = []

        self.create_widgets()

    def create_widgets(self):
        title_label = ttk.Label(self.root, text="Services", font=("Helvetica", 24))
        title_label.pack(pady=10)

        ttk.Label(self.root, text="Select the products you want to service:").pack()

        self.product_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, font=("Helvetica", 12))
        self.product_listbox.pack(fill=tk.BOTH, expand=True)

        for item in item_details.values():
            for product in item.keys():
                self.product_listbox.insert(tk.END, product)

        add_button = ttk.Button(self.root, text="Add to Service", command=self.add_to_service)
        add_button.pack(pady=5)

        remove_button = ttk.Button(self.root, text="Remove from Service", command=self.remove_from_service)
        remove_button.pack(pady=5)

        submit_button = ttk.Button(self.root, text="Submit", command=self.submit_service_request, width=30)
        submit_button.pack(pady=10)

    def add_to_service(self):
        selected_indices = self.product_listbox.curselection()
        for idx in selected_indices:
            item = self.product_listbox.get(idx)
            if item not in self.selected_items:
                self.selected_items.append(item)

    def remove_from_service(self):
        selected_indices = self.product_listbox.curselection()
        for idx in selected_indices:
            item = self.product_listbox.get(idx)
            if item in self.selected_items:
                self.selected_items.remove(item)

    def submit_service_request(self):
        if self.selected_items:
            purchase_history_file = "purchase_history.txt"
            with open(purchase_history_file, "a") as file:
                for item in self.selected_items:
                    service_entry = f"{self.username}: Requested service for {item}\n"
                    file.write(service_entry)
            messagebox.showinfo("Service Requested", "Service requested successfully.")
            self.root.destroy()
        else:
            messagebox.showwarning("No Selection", "Please select at least one item.")



