def bubble_sort():
    flag_cnt = 0
    result = []
    for i in range(A - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                flag_cnt += 1
                if flag_cnt == K:
                    result = [numbers[j], numbers[i]]
                    return result

    return result

A, K = map(int, input().split())
numbers = list(map(int, input().split()))

answer = bubble_sort()
if answer:
    print(*answer)
else:
    print(-1)