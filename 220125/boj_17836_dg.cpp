#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
int map[100][100] = { 0 };
int N, M, T;
int d[8] = { -1,0,0,1,1,0,0,-1 };
int bfs(pair<int,int>start, pair<int,int> end, pair<int,int> gram) {
    // visit
    int visit[100][100] = { 0 };
    int i, j, r, c, dr,dc, nr,nc, dist, ret, tmp;
    // queue
    queue<pair<int, pair<int,int>>> q;
    q.push(make_pair(0, start));
    ret = 100000;
    // bfs
    while (!q.empty()) {
        dist = q.front().first;
        r = q.front().second.first;
        c = q.front().second.second;
        q.pop();
        // if dist is bigger than ret, all value(after the dist in queue) is bigger
        if (dist > ret) break; 
        if (end.first == r && end.second == c) {
            // destination
            ret = min(dist, ret);
            break;
        }
        if (gram.first == r && gram.second == c) {
            // find gram
            tmp = dist + abs(gram.first - N + 1) + abs(gram.second - M + 1);
            ret = min(tmp, ret);
        }
        for (i = 0; i < 4; i++)
        {
            // search in 4 directions
            dr = r + d[2 * i];
            dc = c + d[2 * i + 1];
            if (dr < 0 || dr >= N || dc < 0 || dc >= M) continue;
            if (map[dr][dc] == 1) continue;
            if (visit[dr][dc]) continue;
            visit[dr][dc] = dist + 1;
            q.push(make_pair(dist + 1, make_pair(dr, dc)));
        }
    }
    // time is over
    if (ret > T)
        return -1;
    return ret;
}
int main() {
    // 0 init
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int i, j, ans;
    pair<int, int> gram;
    // 1 input
    cin >> N >> M >> T;
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < M; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 2)
                gram = make_pair(i, j);
        }
    }
    // 2 bfs
    ans = bfs(make_pair(0, 0), make_pair(N-1,M-1), gram);

    // 3 output
    if (ans == -1) {
        cout << "Fail";
    }
    else {
        cout << ans;
    }
    cout << "\n";


    return 0;
}