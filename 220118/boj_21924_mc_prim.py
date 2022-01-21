# 프림 로직을 쓰는데 최소점을 돌리는걸 heapq로 해결하는 법
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
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
# 가중치 시작할 정점 위치
Q = [[0, 1]]
while Q:
    d, u = heappop(Q)
    if visit[u]:
        continue
    visit[u] = 1
    min_cost += d
    for v, w in G[u]:
        if not visit[v]:
            heappush(Q, [w, v])

if sum(visit) == N:
    print(total_cost - min_cost)
else:
    print(-1)

