budget = float(input())
video_card = int(input())
processors = int(input())
ram = int(input())

video_card_price = 250

total_video_card_price = video_card_price * video_card
total_processors_price = processors * (total_video_card_price * 0.35)
total_ram_price = ram * (total_video_card_price * 0.10)

final_sum = total_video_card_price + total_processors_price + total_ram_price

if video_card > processors:
    final_sum *= 0.85


if budget >= final_sum:
    money_left = budget - final_sum
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = final_sum - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")