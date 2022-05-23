import sys
input = sys.stdin.readline

while True:
    try:
        X = int(input())
        wide_x = X * 10000000
        N = int(input())
        block_lst = [int(input()) for _ in range(N)]
        block_lst.sort()
        i = 0
        j = N - 1
        flag = False
        while i < j:
            e1 = block_lst[i]
            e2 = block_lst[j]
            if e1 + e2 == wide_x:
                flag = True
                print(f"yes {e1} {e2}")
                break

            elif e1 + e2 < wide_x:
                i += 1
            else:
                j -= 1

        if not flag:
            print("danger")
    except:
        break

import sys
input = sys.stdin.readline
while True:
    try:
        X = int(input())
        wide_x = X * 10000000
        N = int(input())
        block_lst = []
        for _ in range(N):
            block_lst.append(int(input()))

        block_lst.sort()
        tmp = 0
        e1 = 0
        e2 = 0
        flag = False
        for i in range(N - 1):
            for j in range(i + 1, N):
                tmp1 = block_lst[i]
                tmp2 = block_lst[j]
                if tmp < abs(tmp1 - tmp2) and tmp1 + tmp2 == wide_x:
                    tmp = abs(tmp1 - tmp2)
                    e1 = tmp1
                    e2 = tmp2
                    flag = True

        if flag:
            print(f"yes {e1} {e2}")
        else:
            print("danger")
    except:
        break