N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
print(G)
total_cost = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])
    total_cost += w

visit = [0 for _ in range(N + 1)]
key = [123456789 for _ in range(N + 1)]
# 난 1번부터 돌거임
key[1] = 0
min_cost = 0
for _ in range(1, N + 1):
    u, min_key = 0, 123456789
    for i in range(1, N + 1):
        if not visit[i] and min_key > key[i]:
            u, min_key = i, key[i]
    visit[u] = 1
    min_cost += min_key

    for v, w in G[u]:
        if not visit[v] and key[v] > w:
            key[v] = w

if sum(visit) == N:
    print(total_cost - min_cost)
else:
    print(-1)

# 프림 로직을 쓰는데 최소점을 돌리는걸 heapq로 해결하는 법