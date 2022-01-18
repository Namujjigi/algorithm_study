# import sys; input = sys.stdin.readline

def find(n):
    global parent
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    global rank, parent
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

def cycle_check(a, b):
    global rank, parent
    a, b = find(a), find(b)
    if a == b:
        return True
    union(a, b)
    return False

def kruskal(N, M, adj_list):
    cost = 0
    cnt = 0
    for i in range(M):
        c, a, b = adj_list[i]
        if cycle_check(a, b): continue # ����Ŭ�� ���� ���
        cost += c
        cnt += 1

    if cnt == N - 1: # �ǹ��� N���̹Ƿ� N-1���� ���ΰ� �־����
        return cost
    return -1

def main():
    # 0. �Է�
    global parent, rank
    N, M = map(int, input().split())
    parent = list(range(N + 1))
    rank = [0 for _ in range(N + 1)]
    roads = []
    max_cost = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        roads.append((c, a, b))
        max_cost += c
    roads.sort()
    # 1. �ּ� ����Ʈ��
    ans = kruskal(N, M, roads)
    # 2. ���
    if ans == -1:
        print(-1)
    else:
        print(max_cost - ans)

if __name__ == "__main__":
    main()