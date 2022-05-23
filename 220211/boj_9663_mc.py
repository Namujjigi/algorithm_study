import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def make_abs(num):
    if num < 0:
        return num * -1
    else:
        return num

def is_valid(x):
    i = 0
    while i < x:
        if visit[x] == visit[i]:
            return False
        if (make_abs(visit[x] - visit[i]) == make_abs(x - i)):
            return False
        i += 1

    return True

def make_queen(cnt):
    global ans
    i = 0
    if cnt == N:
        ans += 1
        print(visit[::])
        # return
    else:
        while i < N:
            visit[cnt] = i
            if is_valid(cnt):
                make_queen(cnt + 1)
            i += 1

N = int(input())
ans = 0
visit = [0 for _ in range(N)]
make_queen(0)
print(ans)
