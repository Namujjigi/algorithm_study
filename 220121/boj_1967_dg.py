import sys; input = sys.stdin.readline
from collections import deque
def bfs(start, size, linked_list):
    q = deque([start])
    visit = [-1] * (size + 1)
    visit[start[0]] = 0
    ret = (0, 0)
    while q:
        cur, dist = q.popleft()
        for adj, adj_w in linked_list[cur]:
            if visit[adj] != -1: continue
            visit[adj] = visit[cur] + adj_w
            q.append((adj, visit[adj]))
            if ret[1] < visit[adj]:
                ret = (adj, visit[adj])

    return ret

def main():
    n = int(input())
    linked_list = [list() for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, w = map(int, input().split())
        linked_list[a].append((b, w))
        linked_list[b].append((a, w))

    ret = bfs((1, 0), n, linked_list)
    ans = bfs((ret[0], 0), n, linked_list)
    print(ans[1])

if __name__ == "__main__":
    main()
