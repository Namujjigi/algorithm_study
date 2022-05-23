def find_pal(n):
    # 홀수 길이
    if n % 2:
        left = words[0:n//2]
        right = words[n//2 + 1:n]
    #짝수 길이
    else:
        left = words[0:n//2]
        right = words[n//2:n]
    if left[::] == right[::-1]:
        return False
    return True


words = input()
w_len = len(words)

if find_pal(w_len):
    print(w_len)
elif find_pal(w_len - 1):
    print(w_len - 1)
else:
    print(-1)