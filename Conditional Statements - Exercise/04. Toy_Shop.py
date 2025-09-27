vacation = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

puzzles = puzzle * 2.6
dolls = doll * 3
bears = bear * 4.10
minions = minion * 8.20
trucks = truck * 2

total_toys_sold = puzzle + doll + bear + minion + truck
total_profit = puzzles + dolls + bears + minions + trucks

if total_toys_sold >= 50:
    total_profit *= 0.75

rent = total_profit * 0.10
final_sum = total_profit - rent

if final_sum >= vacation:
    money_left = final_sum - vacation
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = vacation - final_sum
    print(f"Not enough money! {money_needed:.2f} lv needed.")
