Nylon= int(input())
Paint= int(input())
Thinner= int(input())
Hours= int(input())

PaintAdd= Paint * 0.10
NylonAdd= 2
Envelopes= 0.40

NylonPrice= (Nylon + NylonAdd) * 1.50
PaintPrice= (Paint + PaintAdd) * 14.50
ThinnerPrice= Thinner * 5

SumMaterials= NylonPrice + PaintPrice + ThinnerPrice + Envelopes
SumWork= (SumMaterials * 0.30) * Hours

print(SumWork + SumMaterials)