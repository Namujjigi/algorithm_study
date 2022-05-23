import sys
input = sys.stdin.readline

def dfs(v):
    global cnt
    visit[v] = 1
    cnt += 1

    for u in G[v]:
        if visit[u] == 0:
            dfs(u)

for _ in range(int(input())):
    n, m = map(int, input().split())
    visit = [0] * (n + 1)
    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    cnt = 0
    dfs(1)
    print(cnt - 1)