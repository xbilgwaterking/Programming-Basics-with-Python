invalid_num = int(input())

valid_num = (invalid_num >= 100 and invalid_num <= 200) or (invalid_num == 0)

if not valid_num:
    print("invalid")