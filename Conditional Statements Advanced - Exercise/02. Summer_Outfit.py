degrees = int(input())
day_time = input()

top = ""
bottom = ""

if day_time == "Morning":
    if 10 <= degrees <= 18:
        top = "Sweatshirt"
        bottom = "Sneakers"
    elif 18 < degrees <= 24:
        top = "Shirt"
        bottom = "Moccasins"
    else:
        top = "T-Shirt"
        bottom = "Sandals"

elif day_time == "Afternoon":
    if 10 <= degrees <= 18:
        top = "Shirt"
        bottom = "Moccasins"
    elif 18 < degrees <= 24:
        top = "T-Shirt"
        bottom = "Sandals"
    else:
        top = "Swim Suit"
        bottom = "Barefoot"

elif day_time == "Evening":
    if 10 <= degrees <= 18:
        top = "Shirt"
        bottom = "Moccasins"
    else:
        top = "Shirt"
        bottom = "Moccasins"

print(f"It's {degrees} degrees, get your {top} and {bottom}.")