def make_rotation(d_lst, cnt, stop_cnt):
    global directions
    if cnt == stop_cnt:
        directions = d_lst[::]
        return directions

    for i in range(len(d_lst) - 1, -1, -1):
        new_d = (d_lst[i] + 1) % 4
        d_lst.append(new_d)
    make_rotation(d_lst, cnt + 1, stop_cnt)

N = int(input())
visit = [[0 for _ in range(101)] for _ in range(101)]

# 우, 상, 좌, 하
# 0, 1, 2, 3의 방향 설정
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

curve = [list(map(int, input().split())) for _ in range(N)]

for x, y, d, g in curve:
    d_lst = [d]
    directions = []
    make_rotation(d_lst, 0, g)
    visit[y][x] = 1
    for next in directions:
        y += dr[next]
        x += dc[next]
        visit[y][x] = 1

answer = 0
for i in range(101):
    for j in range(101):
        if i + 1 < 101 and j + 1 < 101:
            if visit[i][j] and visit[i + 1][j] and visit[i][j + 1] and visit[i + 1][j + 1]:
                answer += 1

print(answer)