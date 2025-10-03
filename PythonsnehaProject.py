
    # Cafe Management System (Console Project)

# Menu with prices
menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 70,
    "Pizza": 150,
    "Cake": 90
}

order = {}

print("===== Welcome to Python Cafe =====")
print("Here is our Menu:")

for item, price in menu.items():
    print(f"{item:10} - ₹{price}")

print("\nEnter your order (type 'done' when finished):")

while True:
    item = input("Enter item: ").title()
    if item.lower() == "done":
        break
    if item in menu:
        qty = int(input(f"Enter quantity of {item}: "))
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
    else:
        print("❌ Item not available, please choose from menu.")

# Bill generation
print("\n===== BILL RECEIPT =====")
total = 0
for item, qty in order.items():
    price = menu[item] * qty
    total += price
    print(f"{item:10} x{qty} = ₹{price}")

print("---------------------------")
print(f"Total Bill = ₹{total}")
print("===== Thank You! Visit Again =====")
