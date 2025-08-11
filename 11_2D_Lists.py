fruits =     ["cherry", "strawberry", "raspberry", "blueberry"]
vegetables = ["sugarsnaps", "carrot", "cucumber", "bok choy"]
proteins =   ["meatballs", "quorn pieces", "cocktail sausages", "eggs"]
groceries =  [fruits, vegetables, proteins]

print(groceries[1][3])

for collection in groceries:
    for food in collection:
        print(food, end=", ")
    print()



numpad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))

for row in numpad:
    for num in row:
        print(num, end=" ")
    print()