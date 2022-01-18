N, M = map(int, input().split())
trees = list(map(int, input().split()))

s, e = 1, max(trees)

while s <= e:
    m = (s + e) // 2
    total = 0
    for i in trees:
        if i > m:
            total += i - m
    # 나무가 더 많으면 start를 땡겨보는거임
    # 더 적으면 e를 한칸 땡겨봐야함
    # 정확히 일치했다면? 바로 멈춰버리면됨
    if total == M:
        e = m
        break
    elif total > M:
        s = m + 1
    else:
        e = m - 1

print(e)