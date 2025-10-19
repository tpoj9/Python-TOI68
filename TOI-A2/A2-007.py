A = []
B = []

i1 = input().split(" ")
N = int(i1[0])
M = int(i1[1])

for i in range(N):
    i2 = input().split(" ")
    A.append(int(i2[0]))
    B.append(int(i2[1]))

Bucket = []

i1 = input().split(" ")
for i in range(M):
    for j in range(N):
        if A[int(i1[i])-1] > A[j] and B[int(i1[i])-1] < B[j]:
            if not (j+1) in Bucket:
                Bucket.append(j+1)

Bucket.sort()
print(len(Bucket))
for i in Bucket:
    print(i, end=" ")