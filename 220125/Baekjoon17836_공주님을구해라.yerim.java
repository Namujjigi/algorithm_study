package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Baekjoon17836_공주님을구해라 {
	
	static int N,M,T,swordi,swordj,ans;
	static boolean getSword;
	static int[][] castle,visited;
	static int[] di = {-1,1,0,0};
	static int[] dj = {0,0,-1,1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken()); //제한시간
		
		castle = new int[N][M];
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine()," ");
			for(int j=0; j<M; j++) {
				castle[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		visited = new int[N][M];
		getSword = false;
		bfs(0,0);
		
		if(ans == -1 || ans>T) //검이나 공주를 모두 구하지 못한 경우의 수
			System.out.println("Fail");
		else System.out.println(ans);
	}

	private static void bfs(int i, int j) {
		Queue<Point> q = new LinkedList<>();
		q.offer(new Point(0,0,0,getSword));
		visited[0][0] = 1;
		
		ans = -1;
		while(!q.isEmpty()) {
			 Point cur = q.poll();
			 if(cur.i == N-1 && cur.j == M-1) {
				 ans = cur.time;
				 break;
			 }
			 if(!getSword && castle[cur.i][cur.j] == 2) {
				getSword = true;
				q.offer(new Point(cur.i, cur.j, cur.time, true));
			 }

			 for(int d=0; d<4; d++) {
				 int ni = cur.i + di[d];
				 int nj = cur.j + dj[d];
				 if(ni>=0 && ni<N && nj>=0 && nj<M) {
					 if(cur.get && castle[ni][nj]!=3 && visited[ni][nj]<2) {
						 q.offer(new Point(ni, nj, cur.time+1,cur.get));
						 visited[ni][nj]++;
					 }else if(!cur.get && castle[ni][nj]!=1 && visited[ni][nj]==0) {
						 q.offer(new Point(ni, nj, cur.time+1, cur.get));
						 visited[ni][nj]++;
					 }
				 }
			 }
		}
	}
	
	static class Point{
		int i;
		int j;
		int time;
		boolean get;
		public Point(int i, int j, int time, boolean get) {
			this.i = i;
			this.j = j;
			this.time = time;
			this.get = get; //검을 먹은 전인지 후인지 검사하는 함수
		}
	}
}
/*
3 3 100
0 1 2
0 1 1
0 0 0
4


4 4 10
0 0 0 0
0 0 1 0
0 1 2 1
0 0 0 0
6

7 7 100
0 0 0 0 0 0 0
0 1 1 1 1 1 2
0 0 0 0 0 0 0
1 1 1 0 1 1 1
0 0 0 0 0 0 1
0 1 1 1 1 1 1
0 0 0 0 0 0 0
12

4 10 100
0 1 1 1 1 2 1 1 1 1
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0
14
*/
