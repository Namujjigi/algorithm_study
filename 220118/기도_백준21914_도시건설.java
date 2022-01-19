package BaekJun;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

class Node implements Comparable<Node>{
	int x;
	int y;
	int v;
	public Node(int x, int y, int v) {
		super();
		this.x = x;
		this.y = y;
		this.v = v;
	}
	@Override
	public int compareTo(Node o) {
		return this.v - o.v;
	}
	@Override
	public String toString() {
		return "Node [x=" + x + ", y=" + y + ", v=" + v + "]";
	}
	
}
public class BuildCity {
	static int[] parents;
	static Node[] nodes;
	static ArrayList<Node> check;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int N = Integer.parseInt(s[0]);
		int M = Integer.parseInt(s[1]);
		long cost=0;
		parents = new int[N+1]; //부모확인하기 위한 배열
		nodes = new Node[M]; // 간선정보 저장하는 배열
		check = new ArrayList(); // 모든 노드가 이어지는지 확인하는 배열
		long Allcost =0;
		for(int i=0;i<N+1;i++) //초기에는 본인이 부모가 된다
		{
			parents[i]=i;
		}
		for(int i=0;i<M;i++) //간선정보 입력
		{
			s = br.readLine().split(" ");
			nodes[i] = new Node(Integer.parseInt(s[0]),Integer.parseInt(s[1]),Integer.parseInt(s[2]));
			Allcost = Allcost + Integer.parseInt(s[2]);
		}
		Arrays.sort(nodes); //가중치를 기준으로 정렬
		
		for(int i=0;i<M;i++)
		{
			int x = nodes[i].x;
			int y = nodes[i].y;
			int v = nodes[i].v;
			
			int a = find(x); //x노드의 부모찾기
			int b = find(y); //y노드의 부모찾기
			if(a==b) //두 부모가 같으면 싸이클이 생긴다는 뜻이므로 넘김
				continue;
			System.out.println(nodes[i].toString());
			union(x,y); //싸이클이 안생기면 두 정점이 이어졌다는 뜻으로 부모를 합침
			cost = cost+v;
			check.add(nodes[i]); //해당 간선정보를 check배열에 넣기
		}
		Collections.sort(check, new Comparator<Node>() {
			@Override
			public int compare(Node o1, Node o2) {
				return o1.x - o2.x;
			}
		});
		
		for(int i=0;i<check.size();i++) //확인했던 간선정보들을 기준으로 이어져있는지 확인
		{
			int x = check.get(i).x;
			int y = check.get(i).y;
//			System.out.println(check.get(i).toString());
			int a = find(x);
			int b = find(y);
			if(a==b)
				continue;
			
			union(x,y); //모든 노드가 이어져있으면 모든 부모가 같다
		}
		if(connect(N))
			System.out.println(Allcost-cost);
		else
			System.out.println("-1");
		System.out.println(Arrays.toString(parents));
	}
	private static boolean connect(int n) {
		int a = parents[1];
		for(int i=1;i<n+1;i++)
		{
			if(a != parents[i])
				return false;
		}
		return true;
	}
	private static void union(int x, int y) { //두 노드의 부모가 같지 않으면 같게 해줌
		int a = find(x);
		int b = find(y);
		if(a<b) //숫자가 더 낮은 숫자로 부모 결정
			parents[b]=parents[a];
		else if(a>b)
			parents[a]=parents[b];
		else
			return;
	}
	private static int find(int x) { //부모찾기
		if(parents[x]==x)  
			return x;
		else //내가 부모가 아니면 부모의 부모를 찾으러감
		{
			parents[x] = find(parents[x]);
			return parents[x];
		}
	}

}
