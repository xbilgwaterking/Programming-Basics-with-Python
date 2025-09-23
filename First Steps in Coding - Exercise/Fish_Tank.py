Length=int(input())
Width=int(input())
Height=int(input())
Percentage=float(input())

Vloume= Length * Width * Height
Liters= Vloume / 1000
TakenSpace= Percentage / 100

WaterNeeded= Liters * (1 - TakenSpace)

print(WaterNeeded)