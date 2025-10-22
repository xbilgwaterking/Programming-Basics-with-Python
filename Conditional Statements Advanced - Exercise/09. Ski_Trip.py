trip_days = int(input())
place = input()
rate = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

nights = trip_days - 1
price = 0

if place == "room for one person":
    price = room_for_one_person * nights

elif place == "apartment":
    price = apartment * nights
    if trip_days < 10:
        price *= 0.70
    elif 10 < trip_days < 15:
        price *= 0.65
    else:
        price *= 0.50

elif place == "president apartment":
    price = president_apartment * nights
    if trip_days < 10:
        price *= 0.90
    elif 10 < trip_days < 15:
        price *= 0.85
    else:
        price *= 0.80

if rate == "positive":
    price += price * 0.25
else:
    price *= 0.90

print(f"{price:.2f}")
