Sum=float(input())
Period=int(input())
Interest=float(input())

PostInterest= Sum * Interest / 100
MonthlyInterest= PostInterest / 12

print(Sum + Period * MonthlyInterest)
