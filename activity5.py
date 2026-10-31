stock = {"Idly": 20, "Dosa": 15, "Tea": 30}
price = {"Idly": 10, "Dosa": 30, "Tea": 10}

sales = 0

while True:
    item = input("Enter item name (or exit): ")

    if item == "exit":
        break

    qty = int(input("Enter quantity: "))

    if item in stock and qty > 0:
        if qty <= stock[item]:
            bill = qty * price[item]
            stock[item] -= qty
            sales += bill
            print("Bill:", bill)
        else:
            print("Not enough stock")
    else:
        print("Invalid item or quantity")

print("Total Sales:", sales)
print("Remaining Stock:", stock)