# dictionary = a collection of {key:value} pairs. Ordered and changeable, no duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("China"))

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Chicago"})
capitals.pop("USA") # to remove the USA pair
capitals.popitem() # removes latest pair
# capitals.clear() 

keys = capitals.keys()
for key in keys:
    print(key)

values = capitals.values()
for value in values:
    print(value)

items = capitals.items()
for item in items:
    print(item)

for key, value in items:
    print(f"{key}: {value}")