products = {"Pasta": 1.49,
            "Eggs": 2.25,
            "Potato": 0.23,
            "Banana": 0.11,
            "Pizza": 5.00,
            "Lemonade": 1.89,
            "Apple juice": 2.10}

cart = []
total = 0

print()
print("Available products:")
for key, value in products.items():
    print(f"{key:12}: £{value:.2f}")
print()

while True:
    food = input("What item would you like to buy? (q to quit): ").capitalize()
    if food == "Q":
        break
    elif products.get(food) is not None:
        cart.append(food)

print()
print("You have ordered:")
for food in cart:
    total += products.get(food)
    print(food, end=" ")
print()
print()
print(f"Your total is: £{total:.2f}")
print()