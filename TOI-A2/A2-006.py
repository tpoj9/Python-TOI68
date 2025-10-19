n = int(input())
g = []
dp = [[False] * n for _ in range(n)] # สร้าง dp ขนาด n x n และกำหนดค่าเริ่มต้นเป็น False

# อ่าน input และเก็บใน g
for _ in range(n):
    row = input()
    g.append(list(row))

# เริ่มจากปลายทาง ถ้าตำแหน่งขวาล่างเดินได้ ให้เริ่มที่นั่น
if g[n - 1][n - 1] == '.':
    dp[n - 1][n - 1] = True

# ไล่จากล่างขึ้นบน ขวาไปซ้าย
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if i == n - 1 and j == n - 1:
            continue
        if g[i][j] == '.':
            can_go_down = False
            if i + 1 < n:
                can_go_down = dp[i + 1][j]
            can_go_right = False
            if j + 1 < n:
                can_go_right = dp[i][j + 1]
            dp[i][j] = can_go_down or can_go_right

# นับจำนวนตำแหน่งที่สามารถไปถึงปลายทางได้
count = 0
for i in range(n):
    for j in range(n):
        if dp[i][j]:
            count += 1

print(count)
