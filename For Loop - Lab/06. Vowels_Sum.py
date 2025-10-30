words = input()

words_points = 0

for char in words:
    if char == "a":
        words_points += 1
    elif char == "e":
        words_points += 2
    elif char == "i":
        words_points += 3
    elif char == "o":
        words_points += 4
    elif char == "u":
        words_points += 5

print(words_points)
