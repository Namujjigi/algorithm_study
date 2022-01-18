# import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def prim(N, adj_list):
    visit = [False for _ in range(N + 1)]

    h = [(0, 1)] # 1���� N���� ��� �ǹ��� ����Ǿ���ϹǷ� 1���� ����
    ans = 0
    while h:
        cost, cur = heappop(h)
        if visit[cur]: continue
        visit[cur] = True
        ans += cost
        # print(adj_list[cur])
        for adj_cost, adj in adj_list[cur]:
            if not visit[adj]:
                heappush(h, (adj_cost, adj))
    for i in range(1, N + 1):
        if not visit[i]:
            return -1
    return ans

def kruskal(N, M, adj_list):
    pass

def main():
    # 0 �Է�
    N, M = map(int, input().split())
    linked_list = [[] for _ in range(N + 1)]
    max_cost = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        linked_list[a].append((c, b))
        linked_list[b].append((c, a))
        max_cost += c

    # 1 �ּ� ����Ʈ��
    ans = prim(N, linked_list)
    # 2 ���
    if ans == -1:
        print(-1)
    else:
        print(max_cost - ans)

if __name__ == "__main__":
    main()