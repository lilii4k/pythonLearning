# or = at least one condition must be true
# and = both conditions must be true
# not = inverts the condition (not False, not True)

is_sunny = False

#typical if else statement
if is_sunny:
    print("It is sunny!")
else:
    print("It is not sunny.")

#Conditional expressions shorten this:
print("It is sunny!") if is_sunny else print("It is not sunny.")