# while loop = execute some code while some condition remains true.

name = input("Enter name: ")

while name == "":
    print("You did not enter your name.")
    name = input("Enter name: ")

name = name.capitalize()
print(f"Hello {name}")

# for loops = execute a block of code a fixed number of times

for x in reversed(range(1, 11)):
    if x == 5:
        continue
    else:
        print(x)

print(f"Happy New Year {name}!")


# nested loop = a loop within another loop (outer loop, inner loop)
# eg. this code will repeat the inner loop 3 times:
for x in range(3):
    for y in range (1, 10):
        print(y, end="")
    print() # this line starts a new line each repeat