import time

my_time = int(input("Enter time in seconds: "))

countdown = reversed(range(1, my_time+1))

for x in countdown:
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")