result = 0
answer = []
def solution(n, info):
    lion = [0 for _ in range(11)]
    score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    def make_comb(idx, cnt):
        global result, answer
        if idx == -1 and cnt < n:
            return

        if cnt == n:
            lion_score = 0
            apeach_score = 0
            for j in range(11):
                if lion[j] == info[j] == 0:
                    continue
                if lion[j] > info[j]:
                    lion_score += score[j]
                else:
                    apeach_score += score[j]
            if lion_score > apeach_score:
                # 차이가 더 커진경우 값을 갱신
                if lion_score - apeach_score > result:
                    result = lion_score - apeach_score
                    answer = lion[::]
                # 차이가 같은 경우 비교후 갱신
                if lion_score - apeach_score == result:
                    for k in range(10, -1, -1):
                        if answer[k] == lion[k] == 0:
                            continue
                        if answer[k] > lion[k]:
                            break
                        elif answer[k] < lion[k]:
                            answer = lion[::]
                            break
            return

        for i in range(idx, 11):
            lion[i] += 1
            make_comb(i, cnt + 1)
            lion[i] -= 1

    make_comb(0, 0)

    # for an in answer:
    #     print(an)
    # print()

    if answer:
        return answer
    else:
        return [-1]

print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))