import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# r, c 위치
# m 질량/ d 방향 / s 속력
fireballs = []
fire = [[[] for _ in range(N)] for _ in range(N)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])

cnt = 0
while cnt < K:
    while fireballs:
        sr, sc, sm, ss, sd = fireballs.pop()
        nr = (sr + ss * dr[sd]) % N
        nc = (sc + ss * dc[sd]) % N
        fire[nr][nc].append([sm, ss, sd])

    for i in range(N):
        for j in range(N):
            if len(fire[i][j]) == 1:
                nm, ns, nd = fire[i][j].pop()
                fireballs.append([i, j, nm, ns, nd])
            if len(fire[i][j]) > 1:
                f_cnt = 0
                nm = 0
                ns = 0
                d_odd = 0
                d_even = 0
                while fire[i][j]:
                    cm, cs, cd = fire[i][j].pop()
                    nm += cm
                    ns += cs
                    if cd % 2:
                        d_odd += 1
                    else:
                        d_even += 1
                    f_cnt += 1
                if d_odd == f_cnt or d_even == f_cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if nm // 5:
                    for d in nd:
                        fireballs.append([i, j, nm // 5, ns // f_cnt, d])
    cnt += 1

answer = 0
for fi in fireballs:
    answer += fi[2]

print(answer)
