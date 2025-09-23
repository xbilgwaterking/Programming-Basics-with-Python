Pencils=int(input())
Markers=int(input())
Fluid=int(input())
Discount=int(input())

PencilsPrice= Pencils * 5.80
MarkersPrice= Markers * 7.20
FluidPrice= Fluid * 1.20

Sum= PencilsPrice + MarkersPrice + FluidPrice
AfterDiscount= Sum * (Discount / 100)

print(Sum - AfterDiscount)

