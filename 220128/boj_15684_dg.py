import sys; input = sys.stdin.readline
def check(v):
    # check start i to end i
    global N, H
    for i in range(1, N + 1):
        c = i
        for r in range(1, H+1):
            if v[r][c]:
                c += 1
            elif v[r][c - 1]:
                c -= 1
        if c != i:
            return False
    return True

def dfs(ind, x, y, v):
    global answer, N, M, H
    if answer <= ind:
        return
    if check(v):
        answer = min(answer, ind)
        return
    if ind == 3:
        return
    for i in range(y, H + 1):
        for j in range(x, N + 1):
            if v[i][j]: continue
            if v[i][j - 1] or v[i][j + 1]: continue
            v[i][j] = True
            dfs(ind + 1, j, i, v)
            v[i][j] = False
        x = 1

def main():
    global answer, N, M, H
    N, M, H = map(int, input().split())
    ladder = [[False for _ in range(N + 2)] for _ in range(H + 2)]
    for _ in range(M):
        a, b = map(int, input().split())
        ladder[a][b] = True
    answer = 4
    dfs(0, 1, 1, ladder)
    print(-1 if answer == 4 else answer)

if __name__ == "__main__":
    main()