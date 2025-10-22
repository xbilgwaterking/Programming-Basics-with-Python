n1 = int(input())
n2 = int(input())
operator = input()

test = 0
dividable = "even"
non_dividable = "odd"

if n2 == 0:
    print(f"Cannot divide {n1} by zero")
else:
    if operator == "+":
        test = n1 + n2
    elif operator == "-":
        test = n1 - n2
    elif operator == "*":
        test = n1 * n2
    elif operator == "/":
        test = n1 / n2
    elif operator == "%":
        test = n1 % n2

    if ((operator == "+")
            or (operator == "-")
            or (operator == "*")):
        if test % 2 == 0:
            print(f"{n1} {operator} {n2} = {test} - {dividable}")
        else:
            print(f"{n1} {operator} {n2} = {test} - {non_dividable}")

    elif operator == "/":
        print(f"{n1} {operator} {n2} = {test:.2f}")
    else:
        print(f"{n1} {operator} {n2} = {test}")