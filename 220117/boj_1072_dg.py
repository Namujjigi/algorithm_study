def main():
    X, Y = map(int, input().split())
    Z = (Y * 100) // X

    s, e = 0, X
    while s <= e:
        m = (s + e) // 2
        mz = ((Y + m) * 100) // (X + m)
        if mz <= Z: s = m + 1
        else:       e = m - 1

    if s > X:
        print(-1)
    else:
        print(s)

if __name__ == '__main__':
    main()