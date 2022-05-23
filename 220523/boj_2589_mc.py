from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[r][c] = 1
    Q = deque()
    Q.append((r, c))

    tmp = 0
    while Q:
        sr, sc = Q.popleft()

        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 'L' and not visit[nr][nc]:
                visit[nr][nc] = visit[sr][sc] + 1
                if tmp < visit[nr][nc]:
                    tmp = visit[nr][nc]
                Q.append((nr, nc))

    return tmp - 1


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

ans = 0
res = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            res = bfs(i, j)
            if ans < res:
                ans = res

print(ans)