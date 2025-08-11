#Some different things you can do with strings / inputs:
name = (input("Enter name: "))
if name == "":
    print("You didn't enter a name")
    exit()
else:
    next
phone_number = input("Enter a phone number: ")

a = len(name)
b = name.find("l")
c = name.rfind("i")
d = name.capitalize()
e = name.upper()
f = name.lower()
g = name.isdigit()
h = name.isalpha()
phone_number = phone_number.replace("-", "")
i = phone_number.isdigit()


if not i:
    print("Phone number was invalid."), exit()

print(f"Your name is {a} letters long")
print(f"Your name has an l at character {b}") if b >=0 else print("You do not have an l in your name.")
# rfind is just reverse find
print(f"Your name capitalised is {d}")
print(f"Your name in upper case is {e}")
print(f"Your name in lower case is {f}")
print(f"Your name is fully digits.") if g else print("Your name is not fully digits")
print(f"Your name is fully letters.") if h else print("Your name is not fully letters.")