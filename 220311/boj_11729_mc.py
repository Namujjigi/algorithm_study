def hanoi(n, s, e):
    if n == 0:
        return

    hanoi(n - 1, s, 6 - s - e)
    print(s, e)
    hanoi(n - 1, 6 - s - e, e)

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)