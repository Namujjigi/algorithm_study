import sys
input = sys.stdin.readline

N = int(input())
innings = []
for _ in range(N):
    innings.append(list(map(int, input().split())))