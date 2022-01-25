import re

T = int(input())
pattern = re.compile('(100+1+|01)+')

for _ in range(T):
    signal = input()
    if pattern.fullmatch(signal):
        print('YES')
    else:
        print('NO')