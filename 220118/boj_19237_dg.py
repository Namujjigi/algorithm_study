# import sys; input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # �����¿�
def only_one_shark_left():
    global sharks_pos
    for i in range(1, len(sharks_pos)):
        if sharks_pos[i][0] != -1 or sharks_pos[i][1] != -1:
            return False
    return True

def simulate(cnt, k):
    global _map, sharks_dir, sharks_pos, sharks_priority, smell_map
    # 1 ��ȣ ���� ������ �̵�
    for i in range(len(sharks_pos)):
        # ��� ���� �̵����� ����
        if sharks_pos[i][0] == -1 or sharks_pos[i][1] == -1: continue
        # ����� ���� ��ġ
        r, c = sharks_pos[i]
        # 1-1 �켱���� �����ؼ� ���� ���� ĭ���� �̵�
        cur_dir = sharks_dir[i]
        smell_flag = True
        for p_idx in sharks_priority[i][cur_dir]:
            nr = r + d[p_idx][0]
            nc = c + d[p_idx][1]
            if _map[nr][nc] == -1: continue   # ���� ��� ��ġ
            if smell_map[nr][nc][0] != -1 and cnt - smell_map[nr][nc][0] <= k: continue
            # ���� �̹� ��ȴµ� ���� k �ð��� ������ ���� ��� �н�
            # ���� ����� �ʰ�, �ش� �ڸ��� ������ ������ �̵�
            sharks_pos[i][0] = nr
            sharks_pos[i][1] = nc
            sharks_dir[i] = p_idx
            smell_flag = False
            break # �ϳ��� ã�� ��� �ݺ��� ����
        # 1 - 2 ������ ĭ�鿡 ��� ������ �ִ� ���
        if smell_flag:
            for p_idx in sharks_priority[i][cur_dir]:
                nr = r + d[p_idx][0]
                nc = c + d[p_idx][1]
                if _map[nr][nc] == -1: continue   # ���� ��� ��ġ
                if cnt - smell_map[nr][nc][0] <= k and smell_map[nr][nc][1] != i: continue
                # ���� ����� �ʰ� ���� ������� �̵�
                sharks_pos[i][0] = nr
                sharks_pos[i][1] = nc
                sharks_dir[i] = p_idx
                break   # �ϳ��� ã�� ��� �ݺ��� ����


    # 2 �̵��� �� ����. ���� �ڸ��� ������ �ڿ��� ���� ����
    for i in range(len(sharks_pos)-1, -1, -1):
        if sharks_pos[i][0] == -1 or sharks_pos[i][1] == -1: continue
        # �̹� �ش� �ڸ��� �ڱ⺸�� ��ȣ ���� �� �ִ� ��� -1,-1�� �̵�
        for j in range(i):
            if sharks_pos[i] == sharks_pos[j]:
                sharks_pos[i][0] = -1
                sharks_pos[i][1] = -1

    # 3 ���� ����
    for i in range(len(sharks_pos)-1, -1, -1):
        if sharks_pos[i][0] == -1 or sharks_pos[i][1] == -1: continue
        r, c = sharks_pos[i]
        smell_map[r][c][0] = cnt
        smell_map[r][c][1] = i

def main():
    global _map, sharks_dir, sharks_pos, sharks_priority, smell_map
    N, M, K = map(int, input().split())
    smell_map = [[[-1, -1] for _ in range(N + 2)] for _ in range(N + 2)]
    # smell_map[r][c] = [0, 0]: time when the shark visit, shark_index
    _map = []
    _map.append([-1 for _ in range(N + 2)])
    sharks_pos = [[-1, -1] for _ in range(M)]
    # IF sharks_pos[i] = [-1,-1], the shark is already out
    for i in range(N):
        tmp = list(map(int, input().split()))
        _map.append([-1] + tmp + [-1])
        for j in range(N):
            if tmp[j] > 0:
                sharks_pos[tmp[j] - 1][0] = i + 1
                sharks_pos[tmp[j] - 1][1] = j + 1
    _map.append([-1 for _ in range(N + 2)])

    sharks_dir = list(map(lambda x:int(x) - 1, input().split()))
    sharks_priority = [[list(map(lambda x: int(x) - 1, input().split())) for _ in range(4)] for _ in range(M)]


    for i in range(len(sharks_pos)-1, -1, -1):
        if sharks_pos[i][0] == -1 or sharks_pos[i][1] == -1: continue
        r, c = sharks_pos[i]
        smell_map[r][c][0] = 0
        smell_map[r][c][1] = i

    cnt = 0
    while cnt < 1000:
        cnt += 1
        simulate(cnt, K)
        if only_one_shark_left():
            break
    else:
        cnt = -1
    print(cnt)


if __name__ == '__main__':
    main()