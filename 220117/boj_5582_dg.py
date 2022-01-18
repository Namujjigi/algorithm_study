import sys; input = sys.stdin.readline

def main():
    str1, str2 = input().rstrip(), input().rstrip()
    answer = 0
    memo = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for r in range(1, len(str2) + 1):
        for c in range(1, len(str1) + 1):
            if str2[r - 1] == str1[c - 1]:
                memo[r][c] = memo[r - 1][c - 1] + 1
                answer = max(answer, memo[r][c])
            else:
                memo[r][c] = 0
    print(answer)

if __name__ == '__main__':
    main()