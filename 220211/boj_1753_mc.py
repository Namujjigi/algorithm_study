import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

D = [123456789 for _ in range(V + 1)]
D[K] = 0
Q = []
# 가중치 0으로 시작점 heap
heapq.heappush(Q, (0, K))

while Q:
    wei, now = heapq.heappop(Q)

    if wei > D[now]:
        continue

    for node in G[now]:
        dist = D[now] + node[0]
        if dist < D[node[1]]:
            D[node[1]] = dist
            heapq.heappush(Q, ())