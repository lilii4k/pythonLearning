def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(day_of_week(9))


def is_weekend(day):
    match day.lower():
        case "saturday" | "sunday":
            return "It is a weekend"
        case _:
            return "It is not a weekend"

print(is_weekend("Monday"))