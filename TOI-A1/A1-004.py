result = ""
p1 = True
p2 = True
p3 = True

for i in range(3):
    n= int(input())
    if i== 0:
        if n < 5:
            p1 = False
        else:
            p1 = True
    elif i == 1:
        if n < 20:
            p2 = False
        else:
            p2 = True
    elif i == 2:
        if n < 25:
            p3 = False
        else:
            p3 = True
if p1 and p2 and p3:
    print("pass")
else:
    print("fail")