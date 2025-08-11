# collection = single 'variable' used to store multiple values
#   list = [], ordered and changeable
#   set = {}, unordered and immutable, but Add/Remove OK
#   tuple = (), ordered and unchangeable, FASTER

fruits = ["apple", "orange", "banana", "coconut"]
pets = {"dog", "cat", "monkey", "rabbit"}

# print(dir(fruits)) to see all methods available for a collection
# print(help(fruits)) for more info
# print("pineapple" in fruits) # gives True or False to see if an item is in a list or not

fruits.append("pineapple") # adds pineapple to end of list
fruits.remove("pineapple") # removes pineapple from list
fruits.insert(2, "clementine") # adds clementine to list at index 2
fruits.sort() # lists in alphabetical order. when followed by fruits.reverse() it does the opposite order
# fruits.clear clears the list
fruits.index("apple") # gives index of apple
fruits.count("banana") # counts number of banana in list
pets.pop() # prints all except first (random in sets)

# print(fruits[3]) to print a specific item in a list
for fruit in fruits:
    print(fruit) # prints all items in list
for pet in pets:
    print(pets)