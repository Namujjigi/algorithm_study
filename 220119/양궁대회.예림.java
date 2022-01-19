package AlgorithmStudy;

import java.util.Arrays;

public class Programmers_양궁대회 {
	public static void main(String[] args) {
		
//		int n = 5;
//		int[] info = {2,1,1,1,0,0,0,0,0,0,0};
		//[0,2,2,0,1,0,0,0,0,0,0]
//		int n = 1;
//		int[] info = {1,0,0,0,0,0,0,0,0,0,0};
//		//	[-1]
//		int n = 9;
//		int[] info = {0,0,1,2,0,1,1,1,1,1,1};
//		//[1,1,2,0,1,2,2,0,0,0,0]
		int n = 10;
		int[] info = {0,0,0,0,0,0,0,0,3,4,3};
//		//[1,1,1,1,1,1,1,1,0,0,2]
		
		int[] answer = solution(n, info);
		
		for(int i=0; i<answer.length; i++) {
			System.out.print(answer[i]+" ");
		}
	}
	public static int[] solution(int n, int[] info) {
		
		int max = 0;
		int[] answer = new int[11];
		int[] ryans;
		
		for(int i=0; i<(1<<11); i++){
			int cnt = 0;
			int ryan = 0; //라이언의 화살의 개수
			int apeach = 0;
			ryans = new int[11];
	        for(int j=0; j<11; j++) {
	        	if((i&1<<j) != 0) {
	        		cnt += (info[j]+1);
	        		ryan += 10-j;
	        		ryans[j] = info[j]+1;
	        	}else {
	        		ryans[j] = 0;
	        		if(info[j]>0) apeach += 10-j;
	        	}
	        	if(cnt > n) break;
	        }
	        if(cnt<n) {
	        	//채우기
	        	int m = n-cnt;
	        	for(int k=10; k>=0; k--) {
	        		if(info[k]-1 > m) {
	        			ryans[k] = m;
	        			break;
	        		}else {
	        			ryans[k] = info[k]-1;
	        			m -= (info[k]-1);
	        		}
	        	}
	        	cnt = n;
	        }
	        if(cnt==n && (ryan-apeach)>max) {
	        	max = ryan-apeach;
	        	answer = ryans;
	        }else if(cnt==n && (ryan-apeach)==max) {
	        	int preArr = 0; //기존 배열
	        	int newArr = 0;  //새로운 배열
	        	for(int k=10; k>=0; k--) {
	        		preArr += answer[k];
	        		newArr += ryans[k];
	        		if(newArr > preArr) {
	        			answer = ryans;
	        			break;
	        		}
	        	}
	        }
        }
        if(max==0){
            answer = new int[1];
            answer[0] = -1;
            return answer;
        }
        
        return answer;
    }
}
