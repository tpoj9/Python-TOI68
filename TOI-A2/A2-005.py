i1 = input().split(" ")
W = int(i1[0])
H = int(i1[1])
M = int(i1[2])
N = int(i1[3])

i2 = input().split(" ")
for i in range(M):
    i2[i] = int(i2[i])
i2.append(0)
i2.append(W)
i2.sort()

i3 = input().split(" ")
for i in range(N):
    i3[i] = int(i3[i])
i3.append(0)
i3.append(H)
i3.sort()

a = []

for i in range(M+1):
    for j in range(N+1):
        area = (i2[i+1]-i2[i]) * (i3[j+1]-i3[j])
        a.append(area)
a.sort()
print(a[len(a)-1],a[len(a)-2])