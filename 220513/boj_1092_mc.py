n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse = True)
box.sort(reverse = True)

time = 0
box_visit = [0 for _ in range(m)]
count = 0

if box[0] > crane[0]:
    print(-1)
else:
    while count < m:
        crane_visit = [0 for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not box_visit[j] and not crane_visit[i] and box[j] <= crane[i]:
                    crane_visit[i] = 1
                    box_visit[j] = 1
                    count += 1
                    break
        time += 1
    print(time)