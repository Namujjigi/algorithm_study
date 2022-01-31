import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def order(son, parent, son_color):
    global answer
    if color[son] != son_color:
        answer += 1
        son_color = color[son]

    if not len(G[son]):
        return

    for new_son in G[son]:
        if new_son == parent:
            continue
        order(new_son, son, son_color)


N = int(input())
color = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
answer = 0
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

order(1, -1, 0)
print(answer)
