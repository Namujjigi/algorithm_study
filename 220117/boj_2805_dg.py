# import sys; input = sys.stdin.readline

def binary_search_idx(s ,e, trees, goal):
    while s < e:
        m = (s + e) // 2
        if trees[m] == goal:
            return m
        elif trees[m] < goal:
            s = m + 1
        else: # trees[m] > goal
            e = m
    return s

def binary_search(s, e, goal, trees, cumul_sum):
    while s <= e:
        m = (s + e) // 2

        # 1 find a initial height, which is upper value of m
        idx = binary_search_idx(0, len(trees) - 1, trees, m)

        # 2 search cumul_sum of the section over value of m
        tmp_goal = cumul_sum[-1] - cumul_sum[idx] 
        
        # 3 cumul_sum - m * len(the section)
        tmp_goal -= m * (len(cumul_sum) - idx - 1)

        # 4 binary search again
        if tmp_goal >= goal:
            s = m + 1
        else:
            e = m - 1
    
    return e

def main():
    N, M = map(int, input().split())
    trees = sorted(map(int, input().split()))
    cumul_sum = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        cumul_sum[i] = cumul_sum[i - 1] + trees[i - 1]
    
    ret = binary_search(0, trees[N-1], M, trees, cumul_sum)
    print(ret)


if __name__ == "__main__":
    main()