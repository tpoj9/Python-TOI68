n = int(input())
l1 = []
l2 = []
n_stack = 0

for i in range(n):
    l = int(input())
    if l in l1:
        l2[l1.index(l)] += 1
    else:
        l1.append(l)
        l2.append(1)
    
    if l2[l1.index(l)] > n_stack:
        n_stack = l2[l1.index(l)]

print(n_stack)