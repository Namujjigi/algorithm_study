import sys; input = sys.stdin.readline

def main():
    # 0 input
    N, W = map(int, input().split())
    g = [0 for _ in range(N + 1)]
    # if finding nodes have one connection, we find leaves. sometimes include root.
    # if a tree has one root and one leaf, each node has one connection.
    for _ in range(N - 1):
        # calculate the num of connection
        u, v = map(int, input().split())
        g[u] += 1
        g[v] += 1
    g[1] = 0 # remove root node
    # 1 find the num of leaves tree traversal
    num_leaf = sum([n for n in g if n == 1])

    # 2 output
    print(W/num_leaf)


if __name__ == '__main__':
    main()
