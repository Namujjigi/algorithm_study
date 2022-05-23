import sys
input = sys.stdin.readline

N, M, X, Y, K = map(int, input().split())
dice_map = [list(map(int, input().split())) for _ in range(N)]
dir_lst = list(map(int, input().split()))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]