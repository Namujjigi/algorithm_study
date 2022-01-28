#include<iostream>
#include<algorithm>
using namespace std;

int N, M, H;
int ladder[32][12];
int answer;

bool check() {
    int i, r, c;
    for (i = 1; i <= N; i++) {
        c = i;
        for (r = 1; r <= H; r++) {
            if (ladder[r][c] == 1) {
                c++;
            }
            else if (ladder[r][c - 1] == 1) {
                c--;
            }
        }
        if (c != i) {
            return false;
        }
    }
    return true;
}

void dfs(int ind, int x, int y) {
    if (answer <= ind) return;
    if (check()) {
        answer = ind;
        return;
    }
    if (ind == 3) return;

    for (int i = y; i <= H; i++) {
        for (int j = x; j <= N; j++) {
            if (ladder[i][j] == 0 && ladder[i][j - 1] == 0 && ladder[i][j + 1] == 0) {
                ladder[i][j] = 1;
                dfs(ind + 1, j, i);
                ladder[i][j] = 0;
            }
        }
        x = 1;
    }
}

int main() {
    cin >> N >> M >> H;
    int i, a, b;
    for (i = 0; i < M; i++) {
        cin >> a >> b;
        ladder[a][b] = 1;
    }
    answer = 4;
    dfs(0, 1, 1);
    if (answer == 4)
        cout << "-1";
    else
        cout << answer;
}