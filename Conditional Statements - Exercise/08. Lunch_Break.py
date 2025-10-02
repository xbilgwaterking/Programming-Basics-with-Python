import math

serial_name = input()
episode = int(input())
break_time = int(input())

lunch_time = break_time / 8
free_time = break_time / 4

time_left = break_time - lunch_time - free_time

if time_left >= episode:
    enough_time = math.ceil(time_left - episode)
    print(f"You have enough time to watch {serial_name} and left with {enough_time} minutes free time.")
else:
    time_needed = math.ceil(episode - time_left)
    print(f"You don't have enough time to watch {serial_name}, you need {time_needed} more minutes.")