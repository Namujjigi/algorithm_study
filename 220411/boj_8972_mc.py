import sys
input = sys.stdin.readline

def dis_check(s1, r1, s2, r2):
    return abs(s1 - s2) + abs(r1 - r2)

N, M = map(int, input().split())

robots = [list(input().strip()) for _ in range(N)]
move = []
for m in input().strip():
    move.append(int(m))
crazy = []

sr, sc = -1, -1
for i in range(N):
    for j in range(M):
        if robots[i][j] == 'I':
            sr, sc = i, j
        if robots[i][j] == 'R':
            crazy.append([i, j])

dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
kraj_cnt = 0

for idx in range(len(move)):
    # 몇번째 움직임인지 계속 확인
    kraj_cnt = idx

    # 종수 위치 변경
    nr, nc = sr + dr[move[idx] - 1], sc + dc[move[idx] - 1]
    if robots[nr][nc] == 'R':
        break
    robots[sr][sc], robots[nr][nc] = robots[nr][nc], robots[sr][sc]
    sr, sc = nr, nc

    # 종수가 잡혔는지 안 잡혔는지 확인하는 flag
    flag = False
    new_crazy = []
    # 굳이 큐가 아니어도 작업속도 상관없음
    while crazy:
        r, c = crazy.pop()
        temp = 1234568790
        #원래 자리는 .으로 초기화시키고 리스트에서 해결
        robots[r][c] = '.'
        # 미친로봇 다음위치
        pr, pc = -1, -1
        for k in range(9):
            rr, rc = r + dr[k], c + dc[k]
            if 0 <= rr < N and 0 <= rc < M:
                dist = dis_check(sr, sc, rr, rc)
                if temp > dist:
                    temp = dist
                    pr, pc = rr, rc
        new_crazy.append([pr, pc])

    for x, y in new_crazy:
        # 종수가 잡혀서 끝
        if robots[x][y] == 'I':
            flag = True
        # 미친 아두이노가 겹쳐서 폭파
        elif robots[x][y] == 'R':
            robots[x][y] += "R"
        # 미친 아두이노 이동
        elif robots[x][y] == '.':
            robots[x][y] = 'R'

    if flag:
        break

    # 아두이노 위치 추가
    for i in range(N):
        for j in range(M):
            if robots[i][j] == 'R':
                crazy.append([i, j])
            if len(robots[i][j]) > 1:
                robots[i][j] = '.'

if kraj_cnt + 1 == len(move):
    for ro in robots:
        print(''.join(ro), end="\n")
else:
    print("kraj", kraj_cnt + 1)