budget = float(input())
seasons = input()

destination = ""
rest = ""

if budget <= 100:
    destination = "Bulgaria"
    if seasons == "summer":
        rest = "Camp"
        budget *= 0.30
    elif seasons == "winter":
        rest = "Hotel"
        budget *= 0.70

elif budget <= 1000:
    destination = "Balkans"
    if seasons == "summer":
        rest = "Camp"
        budget *= 0.40
    elif seasons == "winter":
        rest = "Hotel"
        budget *= 0.80

elif budget > 1000:
    destination = "Europe"
    if (seasons == "summer"
            or seasons == "winter"):
        rest = "Hotel"
        budget *= 0.90

print(f"Somewhere in {destination}")
print(f"{rest} - {budget:.2f}")
