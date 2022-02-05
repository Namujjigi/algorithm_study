from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    chess = [[0 for _ in range(N)] for _ in range(N)]
    r, c = map(int, input().split())
    gr, gc = map(int, input().split())

    Q = deque()
    Q.append([r, c])
    chess[r][c] = 1

    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]

    while Q:
        sr, sc = Q.popleft()

        if sr == gr and sc == gc:
            break

        for i in range(8):
            nr, nc = sr + dr[i], sc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not chess[nr][nc]:
                chess[nr][nc] = chess[sr][sc] + 1
                Q.append([nr, nc])

    print(chess[gr][gc] - 1)