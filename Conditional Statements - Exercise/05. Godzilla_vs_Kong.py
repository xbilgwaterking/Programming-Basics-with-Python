budget = float(input())
performers = int(input())
outfits = float(input())

stage = budget * 0.10
outfits_price = outfits * performers

if performers > 150:
    outfits_price *= 0.90

movie_sum = stage + outfits_price

if movie_sum > budget:
    money_needed = movie_sum - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")

elif movie_sum <= budget:
    money_left = budget - movie_sum
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
