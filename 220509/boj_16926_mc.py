import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

r, c = N, M
sr, sc = 0, 0
while r > 1 and c > 1:
    rrule = (r * 2) + (c * 2) - 4
    cnt = R % rrule
    rcnt = 0
    while cnt > rcnt:
        pre_value = arr[sr][sc]
        #좌
        for i in range(sr, N - sr - 1):
            tmp = arr[i + 1][sc]
            arr[i + 1][sc] = pre_value
            pre_value = tmp
        #하
        for i in range(sc, M - sc - 1):
            tmp = arr[N - sr - 1][i + 1]
            arr[N - sr - 1][i + 1] = pre_value
            pre_value = tmp
        #우
        for i in range(N - sr - 1, sr, -1):
            tmp = arr[i - 1][M - sc - 1]
            arr[i - 1][M - sc - 1] = pre_value
            pre_value = tmp
        #상
        for i in range(M - sc - 1, sc, -1):
            tmp = arr[sr][i - 1]
            arr[sr][i - 1] = pre_value
            pre_value = tmp
        rcnt += 1

    sr += 1
    sc += 1
    r -= 2
    c -= 2

for ar in arr:
    for a in ar:
        print(a, end=" ")
    print()