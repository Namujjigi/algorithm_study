from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def part_check(newIce):

    visit = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if newIce[i][j] and not visit[i][j]:
                visit[i][j] = cnt + 1
                Q = deque()
                Q.append((i, j))
                while Q:
                    sr, sc = Q.popleft()

                    for k in range(4):
                        nr, nc = sr + dr[k], sc + dc[k]
                        if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and newIce[nr][nc]:
                            visit[nr][nc] = cnt + 1
                            Q.append((nr, nc))
                cnt += 1
            else:
                zero_cnt += 1

    return cnt

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

ans = 0

flag = True
while part_check(ice) < 2 and flag:
    change_stack = []
    for i in range(N):
        for j in range(M):
            if ice[i][j]:
                melt_cnt = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and not ice[nr][nc]:
                        melt_cnt += 1
                change_stack.append((i, j, melt_cnt))

    for r, c, melt in change_stack:
        temp = ice[r][c] - melt
        if temp < 0:
            ice[r][c] = 0
        else:
            ice[r][c] = temp
    ans += 1

    if not part_check(ice):
        flag = False

if flag:
    print(ans)
else:
    print(0)