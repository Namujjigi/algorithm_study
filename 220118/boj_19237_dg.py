# import sys; input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
def only_one_shark_left():
    global sharks_pos
    for i in range(1, len(sharks_pos)):
        if sharks_pos[i][0] != -1 or sharks_pos[i][1] != -1:
            return False
    return True

def simulate(cnt, k):
    global _map, sharks_dir, sharks_pos, sharks_priority, smell_map
    # 1 번호 낮은 상어부터 이동
    for i in range(len(sharks_pos)):
        # 벗어난 상어는 이동하지 않음
        if sharks_pos[i][0] == -1 or sharks_pos[i][1] == -1: continue
        # 상어의 현재 위치
        r, c = sharks_pos[i]
        # 1-1 우선순위 적용해서 냄새 없는 칸으로 이동
        cur_dir = sharks_dir[i]
        smell_flag = True
        for p_idx in sharks_priority[i][cur_dir]:
            nr = r + d[p_idx][0]
            nc = c + d[p_idx][1]
            if _map[nr][nc] == -1: continue   # 맵을 벗어난 위치
            if smell_map[nr][nc][0] != -1 and cnt - smell_map[nr][nc][0] <= k: continue
            # 누가 이미 들렸는데 아직 k 시간이 지나지 않은 경우 패스
            # 맵을 벗어나지 않고, 해당 자리에 냄새가 없으면 이동
            sharks_pos[i][0] = nr
            sharks_pos[i][1] = nc
            sharks_dir[i] = p_idx
            smell_flag = False
            break # 하나라도 찾은 경우 반복문 종료
        # 1 - 2 인접한 칸들에 모두 냄새가 있는 경우
        if smell_flag:
            for p_idx in sharks_priority[i][cur_dir]:
                nr = r + d[p_idx][0]
                nc = c + d[p_idx][1]
                if _map[nr][nc] == -1: continue   # 맵을 벗어난 위치
                if cnt - smell_map[nr][nc][0] <= k and smell_map[nr][nc][1] != i: continue
                # 맵을 벗어나지 않고 본인 냄새라면 이동
                sharks_pos[i][0] = nr
                sharks_pos[i][1] = nc
                sharks_dir[i] = p_idx
                break   # 하나라도 찾은 경우 반복문 종료


    # 2 이동한 뒤 갱신. 같은 자리가 있으면 뒤에서 부터 제거
    for i in range(len(sharks_pos)-1, -1, -1):
        if sharks_pos[i][0] == -1 or sharks_pos[i][1] == -1: continue
        # 이미 해당 자리에 자기보다 번호 낮은 상어가 있는 경우 -1,-1로 이동
        for j in range(i):
            if sharks_pos[i] == sharks_pos[j]:
                sharks_pos[i][0] = -1
                sharks_pos[i][1] = -1

    # 3 냄새 갱신
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