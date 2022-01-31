from collections import deque

N, M, T = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
sword_visit = [[0 for _ in range(M)] for _ in range(N)]

visit[0][0] = 1

Q = deque()
Q.append([0, 0, 0])

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

while Q:
    sr, sc, flag = Q.popleft()
    if maze[sr][sc] == 2:
        sword_visit[sr][sc] = visit[sr][sc]
        flag = 1


    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]
        # 범위 확인
        if 0 <= nr < N and 0 <= nc < M:
            # 칼이 있다면 움직임에 제약 x
            if flag:
                if not sword_visit[nr][nc]:
                    sword_visit[nr][nc] = sword_visit[sr][sc] + 1
                    Q.append([nr, nc, 1])
            # 칼이 없으면 움직임에 제약 o
            if not flag:
                if not visit[nr][nc]:
                    # 벽이 없을 때만 갈 수 있음
                    if maze[nr][nc] == 0:
                        visit[nr][nc] = visit[sr][sc] + 1
                        Q.append([nr, nc, 0])
                    # 칼을 획득 했다면
                    elif maze[nr][nc] == 2:
                        visit[nr][nc] = visit[sr][sc] + 1
                        Q.append([nr, nc, 1])

goal_flag = False
# 둘중에 하나라도 값이 들어가있으면
if visit[N - 1][M - 1] or sword_visit[N - 1][M - 1]:
    goal_flag = True

# 도착못했으면 fail출력
if not goal_flag:
    print('Fail')
else:
    if not visit[N - 1][M - 1]:
        if T >= sword_visit[N - 1][M - 1] - 1:
            print(sword_visit[N - 1][M - 1] - 1)
        else:
            print('Fail')
    elif not sword_visit[N - 1][M - 1]:
        if T >= visit[N - 1][M - 1] - 1:
            print(visit[N - 1][M - 1] - 1)
        else:
            print('Fail')
    else:
        if T >= min(visit[N - 1][M - 1] - 1, sword_visit[N - 1][M - 1] - 1):
            print(min(visit[N - 1][M - 1] - 1, sword_visit[N - 1][M - 1] - 1))
        else:
            print('Fail')
