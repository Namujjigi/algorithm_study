words = input()

cAlpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

tmp = len(words)
idx = 0
ans = 0
while idx < tmp:
    if idx + 3 <= tmp:
        # print("케이스 1111111")
        if words[idx:idx + 3] in cAlpha:
            # print(idx, words[idx:idx + 3], "11111111111")
            ans += 1
            idx += 3
        elif words[idx:idx + 2] in cAlpha:
            # print(idx, words[idx:idx + 2], "222222222222")
            ans += 1
            idx += 2
        else:
            # print(idx, words[idx], "333333333333333")
            ans += 1
            idx += 1
    elif idx + 2 <= tmp:
        # print("케이스 22222222222222")
        if words[idx:idx + 2] in cAlpha:
            # print(idx, words[idx:idx + 2], "222222222222222222")
            ans += 1
            idx += 2
        else:
            # print(idx, words[idx], "333333333333333333")
            ans += 1
            idx += 1
    else:
        # print("케이스 333333")
        # print(idx, words[idx], "333333333333333333")
        ans += 1
        idx += 1
    # print(idx, "연산끝!")
    # print()

print(ans)
