import sys
input = sys.stdin.readline

def backtrack(cnt, idx):
    global temp
    if idx == cnt:
        temp += 1
        for su in sudoku:
            print(*su, end="\n")
        print()
        return

    for i in range(1, 10):
        row, col = blank[idx]
        if temp == 0 and r_check(row, col, i) and c_check(row, col, i) and sq_check(row, col, i):
            sudoku[row][col] = i
            backtrack(cnt, idx + 1)
            sudoku[row][col] = 0

def r_check(row, col, num):
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    return True

def c_check(row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    return True

def sq_check(row, col, num):
    sr = (row // 3) * 3
    sc = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if sudoku[sr + i][sc + j] == num:
                return False
    return True


sudoku = [list(map(int, input().split())) for _ in range(9)]
ans = []
blank = []
cnt = 0
temp = 0
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])
            cnt += 1

backtrack(cnt, 0)