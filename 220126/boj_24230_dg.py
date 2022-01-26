import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def order(cur_node, cur_color, parent, adj_list, color):
    ret = 0
    if color[cur_node] != cur_color:
        ret += 1
        cur_color = color[cur_node]

    if not len(adj_list[cur_node]):
        return ret

    for son in adj_list[cur_node]:
        if son == parent: continue
        ret += order(son, cur_color, cur_node, adj_list, color)

    return ret

def main():
    N = int(input())
    color = [0] + list(map(int, input().split()))
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    ans = order(1, 0, -1, adj_list, color)
    print(ans)

if __name__ == '__main__':
    main()
