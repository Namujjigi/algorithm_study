x, y = map(int, input().split())
z = (y * 100) // x
# 절대 안바뀌는 지점 소수점을 버려서 100이 아닌 99
if z >= 99:
    print(-1)
else:
    result = 0
    s = 0
    e = x
    while s <= e:
        m = (s + e) // 2
        # 계속 이기기만 하는데 같으면 안 바꼈단 소리
        if (y + m) * 100 // (x + m) == z:
            # m보다 값을 하나 땡겨야함
            s = m + 1
        #바꼇다면 result를 갱신하고 혹시 더 적은 판 수가 있는지 확인
        else:
            result = m
            e = m - 1
    print(result)

