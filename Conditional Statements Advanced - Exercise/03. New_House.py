flower_type = input()
flower_quantity = int(input())
budget = int(input())

price = 0
discount = 0
increase = 0

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

if flower_type == "Roses":
    price = roses_price * flower_quantity
    if flower_quantity > 80:
        discount = 0.10
        price -= price * discount

elif flower_type == "Dahlias":
    price = dahlias_price * flower_quantity
    if flower_quantity > 90:
        discount = 0.15
        price -= price * discount

elif flower_type == "Tulips":
    price = tulips_price * flower_quantity
    if flower_quantity > 80:
        discount = 0.15
        price -= price * discount

elif flower_type == "Narcissus":
    price = narcissus_price * flower_quantity
    if flower_quantity < 120:
        increase = 0.15
        price += price * increase

elif flower_type == "Gladiolus":
    price = gladiolus_price * flower_quantity
    if flower_quantity < 80:
        increase = 0.20
        price += price * increase

if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {money_left:.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")