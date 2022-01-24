import sys; input = sys.stdin.readline
import re
p = re.compile('(100+1+|01)+')

def main():
    T = int(input())
    for _ in range(T):
        s = input().rstrip()
        print("YES" if p.fullmatch(s) else "NO")

if __name__ == "__main__":
    main()