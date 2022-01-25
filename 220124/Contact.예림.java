package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon1013_Contact {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		String regex = "(100+1+|01)+";
		for(int i=0; i<N; i++) {
			String str = br.readLine();
			
			//100으로 시작하고 1로 끝나는 숫자 | 01
			if(str.matches(regex)) {
				System.out.println("YES");
			}else System.out.println("NO");
		}
	}
}
/*
1
100111001
*/
