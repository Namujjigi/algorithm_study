from collections import deque
import sys
input = sys.stdin.readline

def make_comb(cnt, pick, visit, idx):
    if cnt == M:
        loc_pick.append(pick[::])
        return

    for i in range(idx, len(loc)):
        if not visit[i]:
            pick.append(i)
            visit[i] = 1
            make_comb(cnt + 1, pick, visit, i + 1)
            visit[i] = 0
            pick.pop()


def find_infec(ans, lo):
    new_lab = [[0 for _ in range(N)] for _ in range(N)]
    Q = deque()
    flag = False
    res = 1
    for idx in lo:
        x, y = loc[idx]
        Q.append((x, y))
        new_lab[x][y] = 1

    while Q:
        sr, sc = Q.popleft()

        for i in range(4):
            nr, nc = sr + dr[i], sc + dc[i]
            if nr >= 0 and nr < N and nc >= 0 and nc < N and lab[nr][nc] != 1 and not new_lab[nr][nc]:
                new_lab[nr][nc] = new_lab[sr][sc] + 1
                Q.append([nr, nc])
                if lab[nr][nc] != 2:
                    res = max(res, new_lab[nr][nc])

    # for la in new_lab:
    #     print(la, end="\n")
    # print(res, "결과!")

    for r in range(N):
        for c in range(N):
            if not new_lab[r][c] and lab[r][c] != 1:
                flag = True

    if flag:
        return 123456789
    else:
        if res - 1 < ans:
            return res - 1
        else:
            return ans

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

loc = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            loc.append((i, j))

ans = 123456789
pick = []
loc_pick = []
comb_visit = [0 for _ in range(len(loc))]
make_comb(0, pick, comb_visit, 0)

temp = 0
for lo in loc_pick:
    temp = find_infec(ans, lo)
    if ans > temp:
        ans = temp

if ans == 123456789:
    print(-1)
else:
    print(ans)