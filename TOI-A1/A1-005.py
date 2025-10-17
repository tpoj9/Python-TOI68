m = int(input())
d = int(input())

if m >= 1 and m <= 3:
    if d >= 21 and m%3 == 0:
        print("spring")
    else:
        print("winter")
elif m >= 4 and m <= 6:
    if d >= 21 and m%3 == 0:
        print("summer")
    else:
        print("spring")
elif m >= 7 and m <= 9:
    if d >= 21 and m%3 == 0:
        print("fall")
    else:
        print("summer")
elif m >= 10 and m <= 12:
    if d >= 21 and m%3 == 0:
        print("winter")
    else:
        print("fall")