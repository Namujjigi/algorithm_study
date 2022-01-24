import re

T = int(input())

for _ in range(T):
    pattern = re.compile('(100+1+|01)+')
    signal = input()
    if pattern.fullmatch(signal):
        print('YES')
    else:
        print('NO')