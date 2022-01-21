import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start, wei):
    global distance
    for v, w in G[start]:
        if not visit[v]:
            visit[v] = 1
            distance[v] = distance[start] + w
            dfs(v, wei + w)

n = int(input())
G = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

# dfs로 다 돌려서 찾기??
# 딱 두번만 돌면됨
# 처음에 아무 점에서 돌려서 가장 먼 곳을 찾고, 그 점에서 돌려서 가장 먼곳을 찾으면 그게 답....
visit = [0] * (n + 1)
distance = [0] * (n + 1)
visit[1] = 1
dfs(1, 0)

first_result = 0
new_start = 0
for i in range(1, n + 1):
    if distance[i] > first_result:
        new_start = i
        first_result = distance[i]

visit = [0] * (n + 1)
distance = [0] * (n + 1)
visit[new_start] = 1
dfs(new_start, 0)
print(max(distance))