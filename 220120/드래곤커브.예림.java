package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon15685_드래곤커브 {
	
	static int[] di = {1,0,-1,0};
	static int[] dj = {0,-1,0,1}; //인덱스 설정...지옥..
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		boolean[][] map = new boolean[101][101];
		int cnt = 0;
		for(int n=0; n<N; n++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			
			int x = Integer.parseInt(st.nextToken()); //시작점 x
			int y = Integer.parseInt(st.nextToken()); //시작점 y
			int d = Integer.parseInt(st.nextToken()); //시작 방향
			int g = Integer.parseInt(st.nextToken()); //세대
			
			//정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것
			//(첫 방향) -> (idx-1) -> 뒤집어! -> (뒤집은방향)+(첫방향)
			StringBuilder sb = new StringBuilder();
			sb.append(d);
			
			int idx = 1;
			for(int i=1; i<=g; i++) {
				for(int j=sb.length()-1; j>=0; j--) {
					int tmpNum = sb.charAt(j)-'0';
					sb.append((tmpNum+1)%4);
				}
			}
			map[y][x] = true;
			for(int j=0; j<sb.length(); j++) {
				int dIdx = sb.charAt(j)-'0';
				x += di[dIdx];
				y += dj[dIdx];
				map[y][x] = true;
			}
		}
		for(int i=0; i<100; i++) {
			for(int j=0; j<100; j++) {
				if(map[i][j] && map[i+1][j+1] && map[i+1][j] && map[i][j+1]) {
					cnt++;
				}
			}
		}
		System.out.println(cnt);
	}
}
