def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

# x = input("What is your first name?: ")
# y = input("What is your surname?: ")
# fullname = create_name(x, y)
# print(f"{fullname} is your name")


# default arguments
import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE")

time_requested = int(input("Input timer length: "))
count(time_requested)

# keyword arguments
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title="Mr.", first="Spongebob", last="Squarepants")

# *args
def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3,4,5,6,7))

# **kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Church Lane", city="Detroit", state="MI", zip="54321")