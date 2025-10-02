import math

world_record = float(input())
meters = float(input())
seconds = float(input())

swimming_time = meters * seconds
delays = math.floor(meters / 15)
water_resistance = delays * 12.5

total_time = swimming_time + water_resistance

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    time_needed = total_time - world_record
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
