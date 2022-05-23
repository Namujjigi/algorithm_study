import sys
input = sys.stdin.readline

def is_valid(lst):
    cnt = 0
    for i in range(2 * N):
        if not lst[i]:
            cnt += 1
    return cnt

N, K = map(int, input().split())
conv = list(map(int, input().split()))
robot = [0 for _ in range(N)]
ans = 0
while is_valid(conv) < K:
    conv = conv[2 * N - 1::] + conv[:2 * N - 1:]
    robot = robot[N - 1::] + robot[:N - 1:]
    robot[-1] = 0
    for i in range(N - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and conv[i + 1] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            conv[i + 1] -= 1
    robot[-1] = 0
    if robot[0] == 0 and conv[0] > 0:
        robot[0] = 1
        conv[0] -= 1
    ans += 1

print(ans)