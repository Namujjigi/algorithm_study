def make_match(start, cnt):
    if cnt == 2:
        match_lst.append(pick[::])
        return

    for i in range(start + 1, 6):
        pick.append(i)
        make_match(i, cnt + 1)
        pick.pop()

def match_result(idx):
    global re
    if idx == 15:
        re += 1
        for k in range(0, 18, 3):
            print(match_result_lst[k:k+3], end='\n')
        print()
        print(re)
        return

    # 0, 1, 2/ 승 무 패
    team1 = match_lst[idx][0]
    team2 = match_lst[idx][1]
    for i in range(3):
        team1_result = i
        team2_result = 2 - i
        match_result_lst[team1 * 3 + team1_result] += 1
        match_result_lst[team2 * 3 + team2_result] += 1
        match_result(idx + 1)
        match_result_lst[team1 * 3 + team1_result] -= 1
        match_result_lst[team2 * 3 + team2_result] -= 1


pick = []
match_lst = []
match_result_lst = [0 for _ in range(18)]
re = 0
make_match(-1, 0)
for ma in match_lst:
    print(ma, end='\n')
print()
match_result(0)