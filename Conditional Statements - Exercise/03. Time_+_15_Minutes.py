hour = int(input())
minutes = int(input())

total_minutes = (hour * 60) + minutes + 15

hours = (total_minutes // 60) % 24
new_minutes = total_minutes % 60

print(f"{hours}:{new_minutes:02d}")
