import sys
input = sys.stdin.readline

def dfs(node):
    G[node] = -2
    for v in new_G[node]:
        dfs(v)

N = int(input())
G = list(map(int, input().split()))
K = int(input())

new_G = [[] for _ in range(N)]

for i in range(N):
    if G[i] == -1:
        continue
    else:
        new_G[G[i]].append(i)

dfs(K)
answer = 0
for j in range(N):
    if G[j] != -2 and j not in G:
        answer += 1

print(answer)