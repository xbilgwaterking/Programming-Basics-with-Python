hour = int(input())
days = input()

if 10 <= hour <= 18:
    if days == "Monday":
        print("open")
    elif days == "Tuesday":
        print("open")
    elif days == "Wednesday":
        print("open")
    elif days == "Thursday":
        print("open")
    elif days == "Friday":
        print("open")
    elif days == "Saturday":
        print("open")
    elif days == "Sunday":
        print("closed")
else:
    print("closed")
