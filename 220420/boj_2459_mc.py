N = int(input())
K = int(input())
pan = [[0 for _ in range(N)] for _ in range(N)]
sr, sc = N - 1, 0
for _ in range(K):
    x, y = map(int, input().split())
    nr = 5 - y
    nc = x - 1
    print("=============")
    print(nr, nc, '꺽이는 위치')
    print("=============")
    if sr == nr:
        print(sc, nc, '들어가는 범위>>>>>>>>>>>>>>')
        if sc < nc:
            for i in range(sc, nc + 1):
                print(sr, i, '찍으면서 갑니다111')
                pan[sr][i] = 1
        else:
            for i in range(sc, nc - 1, -1):
                print(sr, i, '찍으면서 갑니다2222')
                pan[sr][i] = 1
    else:
        print(sr, nr, '들어가는 범위>>>>>>>>>')
        if sr < nr:
            for i in range(sr, nr + 1):
                print(i, sc, "찍으면서 갑니다3333")
                pan[i][sc] = 1
        else:
            for i in range(sr, nr - 1, -1):
                print(i, sc, "찍으면서 갑니다4444")
                pan[i][sc] = 1
    sr, sc = nr, nc
    print()
    print()

cut = int(input())

for pa in pan:
    print(pa, end="\n")