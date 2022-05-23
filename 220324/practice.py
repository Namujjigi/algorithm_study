def make_comb(cnt, n, visit, idx, total_len):
    if cnt == n:
        # print(visit)
        return

    for i in range(idx, total_len):
        if not visit[i]:
            visit[i] = 1
            make_comb(cnt + 1, n, visit, i + 1, total_len)
            visit[i] = 0


def solution(sentences, n):
    word_lst = []
    word_info = []
    for sentence in sentences:
        point = 0
        word_pick = []
        for word in sentence:
            cap = ord(word)
            if 65 <= cap <= 90:
                word_pick.append("shift")
                word_pick.append(chr(cap + 32))
                word_lst.append("shift")
                word_lst.append(chr(cap + 32))
                point += 2
            else:
                if 97 <= cap <= 122:
                    word_pick.append(word)
                    word_lst.append(word)
                point += 1
        word_info.append([point, list(set(word_pick))])
    print(list(set(word_lst)))
    for wi in word_info:
        print(wi, end="\n")
    total_len = len(word_lst)
    print(total_len)
    visit = [0 for _ in range(total_len)]
    make_comb(0, n, visit, 0, total_len)

    answer = -1
    return answer

sentences = ["line in line", "LINE", "in lion"]
n = 5
solution(sentences, n)