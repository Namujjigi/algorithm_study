import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def order(cur_node, parent, graph):
    if cur_node != 1 and len(graph[cur_node]) == 1:
        # leaf node has a connection with parent node
        return 1

    ret = 0
    for son in graph[cur_node]:
        # check child not equal parent, because graph is not tree
        if son == parent: continue
        ret += order(son, cur_node, graph)

    return ret

def main():
    # 0 input
    N, W = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        # bidirectional graph
        # if using tree, check child not equal parent
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 1 find th num of leaves tree traversal
    num_leaf = order(1, -1, g)

    # 2 output
    print(W/num_leaf)


if __name__ == '__main__':
    main()
