class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

shoe_list = []

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                values = map(str.strip, line.split(','))
                shoe_list.append(Shoe(*values))
        print("Data read successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def capture_shoes():
    try:
        values = [input("Enter country: "), input("Enter code: "), input("Enter product: "),
                  float(input("Enter cost: ") or 0.0), int(input("Enter quantity: ") or 0)]
        shoe_list.append(Shoe(*values))
        print("Shoe data captured successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def re_stock():
    try:
        min_line = None
        min_value = float('inf')

        with open("inventory.txt", "r") as file:
            for line_number, line in enumerate(file, start=1):
                numeric_values = [float(value) for value in line.strip().split(',') if value.replace('.', '', 1).isdigit()]
                if numeric_values:
                    current_min_value = min(numeric_values)
                    if current_min_value < min_value:
                        min_line = line.strip()
                        min_value = current_min_value

        if min_line:
            print(min_line)
            new_value = float(input("Enter the value for restocking: "))
            updated_value = min_value + new_value
            print(f"Updated Value after Restocking: {updated_value}")
        else:
            print("No quantity found in the file.")
        print("Thank you for restocking!!")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_shoe():
    try:
        code_to_search = input("Enter the code of the shoe: ")
        found_shoe = next((shoe for shoe in shoe_list if shoe.code == code_to_search), None)
        print(found_shoe) if found_shoe else print("Shoe not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def value_per_item():
    for shoe in shoe_list:
        total_cost_per_item = shoe.cost * shoe.quantity
        print(f"Total cost for {shoe.product} ({shoe.quantity} items on stock): R{total_cost_per_item} with each shoe costing R{shoe.cost}")


def highest_quantity_line():
    max_quantity = float('-inf')

    with open('inventory.txt', 'r') as file:
        for line_number, line in enumerate(file):
            _, _, _, _, quantity_str = line.strip().split(',')
            quantity = int(quantity_str)

            if quantity >= max_quantity:
                max_quantity = quantity
                max_line = line

    stripped = max_line.strip().split(',')
    shoe_sale = stripped[2]
    print(f"The {shoe_sale} is for sale and has a quantity of {max_quantity} pairs in stock")

while True:
    print("\n===== Main Menu =====")
    print("1. Read Shoes Data from File")
    print("2. Capture Shoe Data")
    print("3. View All Shoes")
    print("4. Re-stock Shoes")
    print("5. Search for a Shoe")
    print("6. Calculate Value per Item")
    print("7. Determine Product with Highest Quantity for Sale")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        read_shoes_data()
    elif choice == '2':
        capture_shoes()
    elif choice == '3':
        [print(shoe) for shoe in shoe_list]
    elif choice == '4':
        re_stock()
    elif choice == '5':
        search_shoe()
    elif choice == '6':
        value_per_item()
    elif choice == '7':
        highest_quantity_line()
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
