d1 = int(input())
opr = input().strip()

d2 = (d1%10)*10 + (d1//10)

if opr == '+':
    print(d1,"+",d2, "=", d1 + d2)
elif opr == '*':
    print(d1,"*",d2, "=", d1 * d2)