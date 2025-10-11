product = input()
city = input()
items = float(input())

items_price = 0


if city == "Sofia":
    if product == "coffee":
        items_price = 0.50

    elif product == "water":
        items_price = 0.80

    elif product == "beer":
        items_price = 1.20

    elif product == "sweets":
        items_price = 1.45

    elif product == "peanuts":
        items_price = 1.60

elif city == "Plovdiv":
    if product == "coffee":
        items_price = 0.40

    elif product == "water":
        items_price = 0.70

    elif product == "beer":
        items_price = 1.15

    elif product == "sweets":
        items_price = 1.30

    elif product == "peanuts":
        items_price = 1.50

elif city == "Varna":
    if product == "coffee":
        items_price = 0.45

    elif product == "water":
        items_price = 0.70

    elif product == "beer":
        items_price = 1.10

    elif product == "sweets":
        items_price = 1.35

    elif product == "peanuts":
        items_price = 1.55

to_pay = items * items_price
print(to_pay)
