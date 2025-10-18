min = 0
for i in range(3):
    d = int(input())
    if i == 0:
        min = d
    elif d < min:
        min = d
print(min)