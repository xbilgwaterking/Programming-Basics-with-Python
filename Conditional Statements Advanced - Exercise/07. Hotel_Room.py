month = input()
days = int(input())

studio = 0
apartment = 0


if ((month == "May"
     or month == "October")):
    studio = days * 50
    apartment = days * 65
    if days > 14:
        studio *= 0.70
        apartment *= 0.90
    elif days > 7:
        studio *= 0.95

elif ((month == "June"
      or month == "September")):
    studio = days * 75.20
    apartment = days * 68.70
    if days > 14:
        studio *= 0.80
        apartment *= 0.90

elif ((month == "July"
      or month == "August")):
    studio = days * 76
    apartment = days * 77
    if days > 14:
        apartment *= 0.90

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
