package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Baekjoon1967_트리의지름 {
	
	static ArrayList<Node>[] list;
	static int N, max, totMax;
	static boolean[] check;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		
		list = new ArrayList[N+1];
		for(int i=1; i<=N; i++) {
			list[i] = new ArrayList<>();
		}
		boolean[] haveChild = new boolean[N+1];
		for(int i=1; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");

			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			
			list[start].add(new Node(start, end, weight));
			list[end].add(new Node(end, start, weight));
			haveChild[start] = true;
		}
		max = 0;
		for(int i=1; i<=N; i++) {
			//child가 없는 애들만 또로록 돌리기
			totMax = 0;
			check = new boolean[N+1];
			if(!haveChild[i]) {
				makePath(i,0);
			}
			max = Math.max(totMax, max);
		}
		System.out.println(max);
	}
	public static void makePath(int n, int tot) {
		
		for(int i=0; i<list[n].size(); i++) {
			if(!check[list[n].get(i).end]) {
				check[n] = true;
				makePath(list[n].get(i).end, tot+list[n].get(i).weight);
				check[n] = false;
			}
		}
		totMax = Math.max(tot, totMax);
	}
	
	static class Node{
		int start;
		int end;
		int weight;
		public Node(int start, int end, int weight) {
			this.start = start;
			this.end = end;
			this.weight = weight;
		}
	}
}
/*
5
1 2 33
2 3 34
1 4 22
1 5 10

5
1 3 2
3 4 3
4 2 4
4 5 6

11

3
1 2 3
1 3 50

53

*/
