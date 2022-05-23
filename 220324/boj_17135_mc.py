import sys
from collections import deque
input = sys.stdin.readline

def make_comb(cnt, idx, visit):
    if cnt == 3:
        pick.append(visit[::])
        return

    for i in range(idx, M):
        if not visit[i]:
            visit[i] = 1
            make_comb(cnt + 1, i + 1, visit)
            visit[i] = 0

N, M, D = map(int, input().split())
catsle = [list(map(int, input().split())) for _ in range(N)]

comb_visit = [0 for _ in range(M)]
pick = []
make_comb(0, 0, comb_visit)
# slicing 해서 copy => 로테이션 구현하기
# 사실 1을 0으로 만들 필욘 없을 듯?? 그냥 새로운 [00000]과 나머지를 slicing해서 합쳐주면 안될까?
# idx로 접근해서 어짜피 정해진 턴이라 가능할듯...?
# 사실 로테이션 말고 마지막줄을 없애가면서 올라오는 것도 방법일듯??
# 최대길이 + 1 아닌가?? 거기서 부터 bfs돌리면안될까?

# 아래는 볼 필요가 없음
dr = [0, -1, 0]
dc = [-1, 0, 1]

ans = 0
for loc in pick:
    res = 0
    cnt = 0
    new_catsle = [ca[::] for ca in catsle]
    while cnt < N:
        a_lst = []
        for i in range(M):
            if loc[i]:
                a_lst.append([N - cnt, i])

        remove_pick = []

        # 제거 될 적 위치 찾기
        for ar, ac in a_lst:
            each_pick = []
            Q = deque()
            Q.append((ar, ac, 0))
            visit = [[0 for _ in range(M)] for _ in range(N - cnt)]
            while Q:
                sr, sc, dist = Q.popleft()

                for i in range(3):
                    nr, nc = sr + dr[i], sc + dc[i]
                    if 0 <= nr < N - cnt and 0 <= nc < M and not visit[nr][nc] and dist + 1 <= D:
                        visit[nr][nc] = 0
                        if new_catsle[nr][nc] == 0:
                            Q.append((nr, nc, dist + 1))
                        elif new_catsle[nr][nc] == 1:
                            each_pick.append((nr, nc))
                if each_pick:
                    break

            rr, rc = 123456789, 123456789
            for r, c in each_pick:
                if rc > c:
                    rr, rc = r, c
            if each_pick:
                remove_pick.append((rr, rc))

        # 적 제거하기
        for r, c in remove_pick:
            if new_catsle[r][c] == 1:
                res += 1
            new_catsle[r][c] = 0
        new_catsle.pop()
        cnt += 1

    if ans < res:
        ans = res

print(ans)