package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Baekjoon24230_트리색칠하기 {
	
	static int N, cnt;
	static ArrayList<Integer>[] list;
	static boolean[] visited;
	static int[] color;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		color = new int[N+1];
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		for(int i=1; i<=N; i++) {
			color[i] = Integer.parseInt(st.nextToken()); //각 정점의 색 정보
		}
		list = new ArrayList[N+1];
		for(int i=1; i<=N; i++) {
			list[i] = new ArrayList<>();
		}
		for(int i=1; i<N; i++) { //N-1개의 간선
			st = new StringTokenizer(br.readLine()," ");
			
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			//부모와 자식이 구분된 상태로 입력되지 않기에 우선 두 개 다 넣기
			list[start].add(end);
			list[end].add(start);
		}
		visited = new boolean[N+1];
		cnt = 0;
		if(color[1] != 0) cnt++; //1이 흰색이 아닌 경우에 미리 +1 해주기!
		check(1);
		System.out.println(cnt);
	}
	private static void check(int n) {
		
		visited[n] = true;
		if(list[n].size() == 0) return; //연결된 간선이 없는 경우 바로 return
		
		for(int i=0; i<list[n].size(); i++) {
			int next = list[n].get(i);
			if(!visited[next]) {
				//자식이 부모와 색이 같지 않으면 무조건 자식을 칠해줘야하기 때문에 +1
				//중간에 흰색이 들어가면 반례가 생기려나 했지만 상관없는듯
				if(color[n] != color[next]) cnt++;
				check(next);
			}
		}
	}
}
/*
반례
10
1 1 1 1 2 1 1 2 2 2
3 1
1 4
9 5
10 5
1 2
3 6
3 5
5 8
4 7
*/
