N = int(input())
num_dict = {}

for _ in range(N):
    words = input()
    num_len = len(words) - 1
    temp = 1
    for i in range(num_len, -1, -1):
        if num_dict.get(words[i]):
            num_dict[words[i]] += temp
        else:
            num_dict[words[i]] = temp
        temp *= 10
temp = 9
ans = 0
for num in sorted(num_dict.values(), reverse=True):
    ans += num * temp
    temp -= 1

print(ans)