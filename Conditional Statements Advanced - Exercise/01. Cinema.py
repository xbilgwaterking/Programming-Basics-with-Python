movie_type = input()
rows = int(input())
columns = int(input())

movie_income = 0
movie_clients = rows * columns

if movie_type == "Premiere":
    movie_income = movie_clients * 12
elif movie_type == "Normal":
    movie_income = movie_clients * 7.50
elif movie_type == "Discount":
    movie_income = movie_clients * 5

print(f"{movie_income:.2f}")