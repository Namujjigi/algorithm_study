import sys
from collections import deque
sys = sys.stdin.readline

def dfs(node):
    visit_dfs[node] = 1
    print(node, end=" ")

    for i in range(1, N + 1):
        if not visit_dfs[i] and G[node][i] == 1:
            dfs(i)

def bfs(node):
    Q = deque([node])
    visit_bfs[node] = 1

    while Q:
        now_node = Q.popleft()
        print(now_node, end=" ")

        for i in range(1, N + 1):
            if not visit_bfs[i] and G[now_node][i] == 1:
                visit_bfs[i] = 1
                Q.append(i)


N, M, V = map(int, input().split())

G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

visit_dfs = [0 for _ in range(N + 1)]
visit_bfs = [0 for _ in range(N + 1)]

dfs(V)
print()
bfs(V)