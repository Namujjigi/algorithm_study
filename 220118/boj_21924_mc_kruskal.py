import sys
input = sys.stdin.readline

def findParent(v):
    if v != p[v]:
        p[v] = findParent(p[v])
    return p[v]

N, M = map(int, input().split())

edges = []
total_cost = 0
min_cost = 0
p = [i for i in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append([w, u, v])
    total_cost += w

edges.sort()
new_edges = []

# 우선 가중치를 기준으로 정렬한 후에 min_cost를 찾음
for w, u, v in edges:
    a, b = findParent(u), findParent(v)
    if a != b:
        new_edges.append([u, v])
        p[b] = a
        min_cost += w

new_edges.sort()
# 그 이후에 new_edges를 통해서 부모노드를 통일 시켜줌
# 이때 기준을 찾아야하니까 낮은 번호의 정점을 기준으로 정렬해줌
for u, v in new_edges:
    a, b = findParent(u), findParent(v)
    if a != b:
        p[b] = a

if len(set(p[1::])) == 1:
    print(total_cost - min_cost)
else:
    print(-1)