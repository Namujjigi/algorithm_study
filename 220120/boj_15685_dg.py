# import sys; input = sys.stdin.readline
MAX = 100
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def make_dragon_curve(args):
    r, c, di, g = args
    ret = set()
    vertex = [(r, c), (r + d[di][0], c + d[di][1])] # 0 gen
    ret.add(vertex[0]); ret.add(vertex[1])
    cur_pos = list(vertex[-1])
    for _ in range(g):
        # reverse traversal
        N = len(vertex)
        for i in range(N - 1, 0, -1):
            # find next vertex
            dr = vertex[i][0] - vertex[i - 1][0]
            dc = vertex[i][1] - vertex[i - 1][1]
            ndr = dc
            ndc = -dr
            cur_pos[0] += ndr
            cur_pos[1] += ndc
            vertex.append(tuple(cur_pos))
            ret.add(tuple(cur_pos))
    return ret

def main():
    # 0 input
    N = int(input())
    # 1 input and find vertex in dragon curve
    vertices = set()
    for _ in range(N): # set union
        vertices |= make_dragon_curve(map(int, input().split()))
    # 2 output, check square value
    answer = 0
    for i in range(MAX):
        for j in range(MAX):
            if (i, j) in vertices \
                    and (i, j + 1) in vertices \
                    and (i + 1, j) in vertices \
                    and (i + 1, j + 1) in vertices:
                answer += 1
    print(answer)


if __name__ == '__main__':
    main()