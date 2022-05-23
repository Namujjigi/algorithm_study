import sys
from collections import deque
input = sys.stdin.readline

# 탐색 후에 .으로 변환까지 다 진행시킴
def bfs(r, c, color):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    visit = [[0 for _ in range(6)] for _ in range(12)]
    cnt = 1
    pick = []
    Q = deque()
    Q.append((r, c))
    visit[r][c] = 1
    pick.append((r, c))

    while Q:
        sr, sc = Q.popleft()

        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if 0 <= nr < 12 and 0 <= nc < 6 and not visit[nr][nc] and puyo[nr][nc] == color:
                visit[nr][nc] = 1
                Q.append((nr, nc))
                pick.append((nr, nc))
                cnt += 1
    if cnt >= 4:
        for i, j in pick:
            puyo[i][j] = '.'
        return True
    else:
        return False

# 밑으로 내려가게 함
def down_puyo():
    # 가장 아래는 볼 필요가 없음
    for i in range(10, -1, -1):
        for j in range(6):
            if puyo[i][j] != '.' and puyo[i + 1][j] == '.':
                r, c = i , j
                while (0 <= r < 11) and puyo[r + 1][c] == '.':
                    puyo[r][c], puyo[r + 1][c] = puyo[r + 1][c], puyo[r][c]
                    r += 1

puyo = [list(input().strip()) for _ in range(12)]
ans = 0

while True:
    d_flag = False
    flag = False
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                d_flag = bfs(i, j, puyo[i][j])
                if d_flag:
                    flag = True
    if flag:
        down_puyo()
        ans += 1
    else:
        break

print(ans)