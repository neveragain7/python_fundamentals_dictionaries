orders = {}

command = input()

while not command == "buy":
    data = command.split()
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product not in orders:
        orders[product] = {"price": price, "quantity": quantity}
    else:
        orders[product]["price"] = price
        orders[product]["quantity"] += quantity

    command = input()

for key, value in orders.items():
    final_price = value["price"] * value["quantity"]
    print(f"{key} -> {final_price:.2f}")
