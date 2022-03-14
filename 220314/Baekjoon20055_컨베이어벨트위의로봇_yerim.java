package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Baekjoon20055_컨베이어벨트위의로봇 {
	
	static int[] belt;
	static boolean[] boxCheck;
	static int N, K;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		belt = new int[2*N];
		boxCheck = new boolean[2*N];
		st = new StringTokenizer(br.readLine()," ");
		for(int i=0; i<2*N; i++) {
			belt[i] = Integer.parseInt(st.nextToken());
		}
		int cnt = 0;
		int idx = 0;
		int step = 0;
		while(true) {
			
			step++;
			//1. 벨트 움직이기 (올리는 위치를 나타내는 idx를 바꾸기)
			if(idx==0) idx = N*2-1;
			else idx--;
			//2. 벨트가 회전하는 방향으로 한 칸 이동
			boxCheck[(idx+N-1)%(2*N)] = false; //N번째 벨트에서 박스 내리기
			for(int i=N-2; i>=0; i--) {
				//한 칸씩 옮기고 N-1에 있는 박스들 다 내리기
				int checkIdx = (idx+i)%(N*2);
				int nextIdx = (idx+i+1)%(N*2);
				if(boxCheck[checkIdx] && !boxCheck[nextIdx] && belt[nextIdx]>0) {
					boxCheck[nextIdx] = true;
					boxCheck[checkIdx] = false;
					belt[nextIdx]--;
					if(belt[nextIdx]==0) cnt++;
				}
			}
			boxCheck[(idx+N-1)%(2*N)] = false; //로봇을 옮긴후에 또 내리는 곳에서 로봇 내려줘야함
			//3. 올리는 위치의 칸의 내구도가 0이 아니면 로봇을 올린다.
			if(belt[idx]>0) {
				belt[idx]--;
				boxCheck[idx] = true;
				if(belt[idx]==0) cnt++;
			}
			//4. 내구도 0인 칸 체크
			if(cnt>=K) break;
		}
		System.out.println(step);
	}
}
