import sys
input = sys.stdin.readline

A, K = map(int, input().split())
numbers = list(map(int, input().split()))

result = []
cnt = 0
for i in range(A):
    for j in range(A - i - 1):
        if numbers[j] > numbers[j + 1]:
            cnt += 1
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            if cnt == K:
                result = [numbers[j], numbers[j + 1]]

if result:
    print(*result)
else:
    print(-1)