import sys; input = sys.stdin.readline
import re
p = re.compile('(100+1+|01)+')

def pattern_check(s):
    i = 0
    while i < len(s):
        m = p.match(s[i:])
        if not m:
            return False
        if m.end() == len(s):
            return True
        if s[m.end() - 1] == '1':
            if s[m.end() - 2] == '1':
                i += m.end() - 1
            else:
                i += m.end()
        else:
            i += m.end()

    return True

def main():
    T = int(input())
    for _ in range(T):
        s = input().rstrip()
        if pattern_check(s):
            print("YES")
        else:
            print("NO")



if __name__ == "__main__":
    main()

