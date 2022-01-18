package AlgorithmStudy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon5582_공통부분문자열 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s1 = br.readLine();
		String s2 = br.readLine();
		
		char[] text1 = s1.toCharArray();
		char[] text2 = s2.toCharArray();
		
		int len1 = text1.length;
		int len2 = text2.length;
		
		int max = 0;
		int[][] dp = new int[len1][len2];
		for(int i=0; i<len1; i++) {
			for(int j=0; j<len2; j++) {
				if(text1[i] == text2[j]) {
					dp[i][j]++;
					if(i-1>=0 && j-1>=0 && dp[i-1][j-1]>0) dp[i][j] += dp[i-1][j-1];
					
					max = Math.max(max, dp[i][j]);
				}
			}
		}
		System.out.println(max);
	}
}
/*
ECADADABRBCRDARA
ABRACADABRA
 */
