N = int(input())
K = int(input())
loc = list(map(int, input().split()))
loc.sort()

if N <= K:
    print(0)
else:
    dist = []
    for i in range(N - 1):
        dist.append(loc[i + 1] - loc[i])

    dist.sort()

    for j in range(K - 1):
        dist.pop()

    print(sum(dist))