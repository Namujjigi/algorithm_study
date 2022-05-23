import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

r = 0
c = 0
while r < N // 2 and c < M // 2:
    cnt = R % (((N - (r * 2)) + (M - (c * 2))) * 2 - 4)
    spin_cnt = 0
    while spin_cnt < cnt:
        tmp = arr[r][c]
        for i in range(c, M - 1 - c):
            arr[r][i] = arr[r][i + 1]

        for j in range(r, N - 1 -r):
            arr[j][M - c - 1] = arr[j + 1][M - c - 1]

        for k in range(M - 1 - c, 0 + c, -1):
            arr[N - r - 1][k] = arr[N - r - 1][k - 1]

        for l in range(N - 1 - r, 1 + r, -1):
            arr[l][c] = arr[l - 1][c]

        arr[r + 1][c] = tmp
        spin_cnt += 1
    r += 1
    c += 1

for a in arr:
    print(*a, end="\n")