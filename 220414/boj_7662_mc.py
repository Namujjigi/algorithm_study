import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    Q = deque()
    for _ in range(K):
        order, num = input().split()
        if order == 'I':
            Q.append(int(num))
            Q = sorted(Q)
            print(int(num), '들어온 숫자', Q, 'Q의 변화')
        elif order == 'D':
            print(Q, '삭제 예정입니다', num, '의 값이')
            if not Q:
                continue
            else:
                if num == '-1':
                    Q.popleft()
                else:
                    Q.pop()
    print()