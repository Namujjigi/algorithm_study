from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(''.join(input())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

Q = deque()

visit =[[0 for _ in range(M)] for _ in range(N)]


visit[0][0] = 1
Q.append([0, 0])

while Q:
    sr, sc = Q.popleft()

    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc]:
            if maze[nr][nc] == '1':
                visit[nr][nc] = visit[sr][sc] + 1
                Q.append([nr, nc])

print(visit[N - 1][M - 1])