R, C = map(int, input().split())
wall = list(map(int, input().split()))
space = [[0 for _ in range(C)] for _ in range(R)]

c_idx = 0
for w in wall:
    for i in range(R - 1, R - w - 1, -1):
        space[i][c_idx] = 1
    c_idx += 1

ans = 0
for i in range(R):
    for j in range(C - 1):
        if space[i][j] == 1 and space[i][j + 1] == 0:
            cr, cc = i, j + 1
            tmp = 0
            # 벽때문에 끝났는지 범위를 벗어나서 끝났는지
            while cc < C and space[cr][cc] == 0:
                tmp += 1
                cc += 1
            if cc < C and space[cr][cc] == 1:
                ans += tmp
print(ans)