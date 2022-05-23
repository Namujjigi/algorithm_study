import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
mirror = [list(map(str, input().strip())) for _ in range(N)]
# . 아무것도 없음 빛 통과 o
# ! 거울 설치 가능
# * 벽 빛 통과 x
# 거울에 비친 빛은 양방향 전부 다 간다

# 동 남 서 북
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
visit = [[[0 for _ in range(4)] for _ in range(N)] for _ in range(N)]

br, bc, er, ec = -1, -1, -1, -1

# 도착점 끝점 뽑기
for i in range(N):
    for j in range(N):
        if mirror[i][j] == '#':
            if br == -1:
                br, bc = i, j
            else:
                er, ec = i, j

Q = deque()

# 시작 방향 찾기
dir = -1
for i in range(4):
    r, c = br + dr[i], bc + dc[i]
    if 0 <= r < N and 0 <= c < N and mirror[r][c] != "*":
        visit[br][bc][i] = 1
        Q.append([br, bc, i])

ans = []
while Q:
    sr, sc, d = Q.popleft()

    nr, nc = sr + dr[d], sc + dc[d]
    if 0 <= nr < N and 0 <= nc < N and mirror[nr][nc] != '*':
        visit[nr][nc][d] = visit[sr][sc][d]
        # 도착 지점 온거라면?
        if nr == er and nc == ec:
            ans.append(visit[nr][nc][d])
        # 거울 설치만 따로 추가
        elif mirror[nr][nc] == '!':
            # 꺽이는 방향 2개
            ndir = [(d + 1) % 4, (d + 3) % 4]
            for nd in ndir:
                if not visit[nr][nc][nd] or visit[nr][nc][nd] > visit[sr][sc][d] + 1:
                    visit[nr][nc][nd] = visit[sr][sc][d] + 1
                    Q.append([nr, nc, nd])
        # 진행방향으로 그대로 진행하기
        Q.append([nr, nc, d])

print(min(ans) - 1)