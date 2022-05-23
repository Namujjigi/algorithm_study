def valid_check(arr, equ):
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] == equ:
            return True
        if arr[0][i] == arr[1][i] == arr[2][i] == equ:
            return True
    if arr[0][0]==arr[1][1]==arr[2][2]==equ:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==equ:
        return True
    return False

while True:
    ttt = input()
    if ttt == "end":
        break
    x_cnt = 0
    o_cnt = 0
    b_cnt = 0
    ttt_lst = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(9):
        r = i // 3
        c = i % 3
        ttt_lst[r][c] = ttt[i]
        if ttt[i] == 'X':
            x_cnt += 1
        elif ttt[i] == 'O':
            o_cnt += 1
        elif ttt[i] == '.':
            b_cnt += 1

    # 공백이 하나도 없으면
    if b_cnt == 0:
        if x_cnt == 5 and o_cnt == 4:
            if not valid_check(ttt_lst, 'O'):
                print("valid")
            else:
                print("invalid")
        else:
            print("invalid")
    # 공백이 있는 경우
    else:
        if x_cnt == o_cnt + 1:
            if not valid_check(ttt_lst, 'O') and valid_check(ttt_lst, 'X'):
                print("valid")
            else:
                print("invalid")
        elif x_cnt == o_cnt:
            if valid_check(ttt_lst, 'O') and not valid_check(ttt_lst, 'X'):
                print("valid")
            else:
                print("invalid")
        else:
            print("invalid")