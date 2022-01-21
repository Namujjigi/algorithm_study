#include<iostream>
#include<vector>
using namespace std;
#define INF 987654321
#define min(x, y) (x > y) ? y : x
#define max(x, y) (x > y) ? x : y
int N;
vector<vector<int>> adj_arr;

int floyd_warshall(){
    int i, j, k, max_val = 0;
    // floyd_warshall algorithm
    // find all nodes to all nodes
    for (k = 1; k <= N; k++){
        for (i = 1; i <= N; i++){
            for (j = 1; j <= N; j++){
                adj_arr[i][j] = min(
                    adj_arr[i][j],
                    adj_arr[i][k] + adj_arr[k][j]
                );
            }
        }
    }
        
    // find max value, not INF
    for (i = 1; i <= N; i++)
        for (j = 1; j <= N; j++) 
            if (adj_arr[i][j] != INF)
                max_val = max(max_val, adj_arr[i][j]);
    return max_val;
}

int main(){

    // 0 input
    int i, a, b, w;
    cin >> N;
    adj_arr = vector<vector<int>> (N + 1, vector<int> (N + 1, INF));
    for (i = 1; i <= N; i++)
        adj_arr[i][i] = 0;
    for (i = 0; i < N - 1; i++){
        cin >> a >> b >> w;
        adj_arr[a][b] = w;
        adj_arr[b][a] = w;
    }
    // 1 find output
    cout << floyd_warshall() << '\n';
    return 0;
}
