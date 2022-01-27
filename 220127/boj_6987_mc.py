# 현재 나라, 상대할 적, 결과, 경기 수 판단
def backtrack(country, opponent, cnt):
    if country == 5:
        print('전적학인')
        for ma in match:
            print(ma, end='\n')
        print()
        return

    elif opponent == 6:
        backtrack(country + 1, country + 2, 0)

    # 0, 1, 2 / 승 무 패
    elif cnt < 5 - country:
        if not visit[country][opponent]:
            visit[country][opponent] = 1
            for i in range(3):
                match[country][i] += 1
                match[opponent][2 - i] += 1
                backtrack(country, opponent + 1, cnt + 1)
                match[country][i] -= 1
                match[opponent][2 - i] -= 1
            visit[country][opponent] = 0

match = [[0 for _ in range(3)] for _ in range(6)]
visit = [[0 for _ in range(6)] for _ in range(6)]

backtrack(0, 1, 0)

