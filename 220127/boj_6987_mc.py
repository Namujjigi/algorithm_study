def make_match(start, cnt):
    if cnt == 2:
        match_lst.append(pick[::])
        return

    for i in range(start + 1, 6):
        pick.append(i)
        make_match(i, cnt + 1)
        pick.pop()

def match_result(idx):
    global answer
    if idx == 15:
        if not sum(match):
            answer = 1
        else:
            answer = 0
            return
        return

    # 0, 1, 2/ 승 무 패
    team1 = match_lst[idx][0]
    team2 = match_lst[idx][1]
    for i in range(3):
        team1_result = i
        team2_result = 2 - i
        if match[team1 * 3 + team1_result] > 0 and match[team2 * 3 + team2_result] > 0:
            match[team1 * 3 + team1_result] -= 1
            match[team2 * 3 + team2_result] -= 1
            match_result(idx + 1)
            match[team1 * 3 + team1_result] += 1
            match[team2 * 3 + team2_result] += 1


pick = []
match_lst = []
make_match(-1, 0)
ans_lst = []
for _ in range(4):
    match = list(map(int, input().split()))
    answer = 0
    match_result(0)
    ans_lst.append(answer)

print(*ans_lst)