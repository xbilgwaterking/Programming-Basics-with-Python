budget = int(input())
seasons = input()
people = int(input())

price = 0
discount = 0
ship_price = 0

if seasons == "Spring":
    ship_price = 3000

    if people <= 6:
        ship_price *= 0.90
    elif 7 <= people <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75

elif seasons == "Summer":
    ship_price = 4200

    if people <= 6:
        ship_price *= 0.90
    elif 7 <= people <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75

elif seasons == "Autumn":
    ship_price = 4200

    if people <= 6:
        ship_price *= 0.90
    elif 7 <= people <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75

elif seasons == "Winter":
    ship_price = 2600

    if people <= 6:
        ship_price *= 0.90
    elif 7 <= people <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75

if ((seasons == "Spring")
        or (seasons == "Summer")
        or (seasons == "Winter")):
    if people % 2 == 0:
        ship_price *= 0.95

if budget >= ship_price:
    money_left = budget - ship_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = ship_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")