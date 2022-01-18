package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Baekjoon21924_도시건설 {
	
	static ArrayList<Tower>[] list;
	static int N, M;
	static PriorityQueue<Tower> pq;
	static boolean[] building;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		list = new ArrayList[N+1];
		
		for(int i=1; i<=N; i++) {
			list[i] = new ArrayList<>();
		}
		
		long tot = 0; //long............
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine()," ");
			
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int dis = Integer.parseInt(st.nextToken());
			
			list[from].add(new Tower(from, to, dis));
			list[to].add(new Tower(to, from, dis));
			
			tot += dis;
			
		}
		building = new boolean[N+1];
		pq = new PriorityQueue<>();
		Put(1); //임의의 출발점
		building[1] = true;
		
		int cnt = 1;
		while(true) {
			
			Tower cur = pq.poll();
			
			if(!building[cur.to]) {
				building[cur.to] = true;
				tot -= cur.dis;
				Put(cur.to);
				cnt++;
			}
			
			if(pq.isEmpty() && cnt<N) {
				tot = -1;
				break;
			}
			if(cnt == N) break;
			
		}
		System.out.println(tot);
		
	}
	public static void Put(int start) {
		
		int size = list[start].size();
		
		for(int i=0; i<size; i++) {
			pq.offer(list[start].get(i));
		}
	}
	
	static class Tower implements Comparable<Tower>{
		int from;
		int to;
		int dis;
		public Tower(int from, int to, int dis) {
			this.from = from;
			this.to = to;
			this.dis = dis;
		}
		@Override
		public int compareTo(Tower o) {
			return this.dis-o.dis;
		}
	}
}
