def answer_change(before, after):
    for i in range(11 - 1, -1, -1):
        if before[i] == after[i]:
            continue
        elif before[i] > after[i]:
            return False
        else: #before[b_idx] < after[a_idx]
            return True
    return False

def backtrack(ind, time, limit, apeach, r_score, a_score):
    global ryan, answer, max_score
    if time == limit: #
        diff_score = r_score - a_score
        if diff_score > 0: # ryan win
            if max_score < diff_score:
                max_score = diff_score
                answer = ryan[:]
            elif max_score == diff_score: # renew
                if answer_change(answer, ryan):
                    answer = ryan[:]
        return

    if ind == 10: # 끝까지 간 경우
        ryan[ind] = limit - time
        backtrack(ind + 1, limit, limit, apeach, r_score, a_score)
        ryan[ind] = 0
        return

    # 라이언이 이기는 경우
    X = apeach[ind] + 1
    if X <= limit - time: # 발사 횟수를 넘지 않는 경우만 탐색
        ryan[ind] = X
        backtrack(
            ind + 1, time + X, limit, apeach,
            # ryan한테 점수 추가
            r_score + (10 - ind),
            # apeach가 맞춘적이 있으면 점수 제거
            a_score - (10 - ind) if apeach[ind] else a_score
        )
        ryan[ind] = 0

    # 라이언이 지거나 무시하는경우 점수 변동 없음
    backtrack(ind + 1, time, limit, apeach, r_score, a_score)



def solution(n, info):
    global ryan, answer, max_score
    answer = [-1]
    max_score = 0
    ryan = [0 for _ in range(11)]
    init_a_score = 0
    for i in range(10):
        init_a_score += 10 - i if info[i] else 0

    backtrack(0, 0, n, info, 0, init_a_score)

    return answer

if __name__ == '__main__':
    io = [
        [5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]],
        # [1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1]],
        # [9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1], [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]],
        # [10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]],
        # [3, [1, 1, 0, 0, 0, 0, 0, 0, 3, 4, 3], [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]],
    ]
    for n, info, result in io:
        print(solution(n, info) == result)

# [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
# [1, 1, 1, 1, 1, 1, 0, 0, 4, 0, 0]