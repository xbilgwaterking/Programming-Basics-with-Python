Pages=int(input())
PagesPerHour=int(input())
Days=int(input())

Hours= Pages / PagesPerHour
HoursPerDay= Hours / Days

print(int(HoursPerDay))