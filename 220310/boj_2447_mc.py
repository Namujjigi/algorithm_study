def make_star(n):
    if n == 3:
        stars[0][:3] = stars[2][:3] = ['*', '*', '*']
        stars[1][:3] = ['*', ' ', '*']
        return

    idx = n // 3
    make_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(idx):
                stars[idx * i + k][idx * j:idx * (j + 1)] = stars[k][:idx]

N = int(input())
stars = [[' ' for _ in range(N)] for _ in range(N)]
make_star(N)
for star in stars:
    print(''.join(star), end="\n")