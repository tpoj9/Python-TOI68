n = input()
b = 0
tree = input().split(" ")
for i in range(int(n)):
    tree[i] = int(tree[i])

for i in range(int(n)):
    if i == 0:
        if tree[i] > tree[i + 1]:
            b += 1
    elif i == int(n) - 1:
        if tree[i] > tree[i - 1]:
            b += 1
    else:
        if tree[i] > tree[i - 1] and tree[i] > tree[i + 1]:
            b += 1
print(b)