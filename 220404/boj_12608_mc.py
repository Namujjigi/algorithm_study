import sys
input = sys.stdin.readline

def check_seat(idx, student):
    like_cnt = -1
    empty_cnt = -1
    pick = [0, 0]

    for sr in range(N):
        for sc in range(N):
            if not cla[sr][sc]:
                like_tmp = 0
                empty_tmp = 0
                for k in range(4):
                    nr, nc = sr + dr[k], sc + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if cla[nr][nc] in like_lst[idx]:
                            like_tmp += 1
                        if not cla[nr][nc]:
                            empty_tmp += 1
                # 1. 좋아하는 학생이 더 많을 경우
                if like_tmp > like_cnt or (like_tmp == like_cnt and empty_tmp > empty_cnt):
                    like_cnt = like_tmp
                    empty_cnt = empty_tmp
                    pick[0], pick[1] = sr, sc

    # 최종 선정된 자리에 해당 학생 배치
    r, c = pick[0], pick[1]
    cla[r][c] = student
    return


N = int(input())
stu_lst = []
like_lst = []
for _ in range(N ** 2):
    info_lst = list(map(int, input().split()))
    stu_lst.append(info_lst[0])
    like_lst.append(info_lst[1::])

dr = [0, -1, 1, 0]
dc = [-1, 0, 0, 1]

cla = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N ** 2):
    check_seat(i, stu_lst[i])

ans = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for idx in range(N ** 2):
            if cla[r][c] == stu_lst[idx]:
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if cla[nr][nc] in like_lst[idx]:
                            cnt += 1
        if cnt >= 1:
            ans += 10 ** (cnt - 1)

print(ans)