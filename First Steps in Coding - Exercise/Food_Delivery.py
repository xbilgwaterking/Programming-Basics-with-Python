ChickenMenu=int(input())
FishMenu=int(input())
VeganMenu=int(input())


ChickenMenuPrice= ChickenMenu * 10.35
FishMenuPrice= FishMenu * 12.40
VeganMenuPrice= VeganMenu * 8.15

Food= ChickenMenuPrice + FishMenuPrice + VeganMenuPrice

Delivery= 2.50
Dessert= Food * 0.20

print(Food + Dessert + Delivery)
