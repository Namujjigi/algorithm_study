import java.util.Arrays;
class Solution {
    static int max =Integer.MIN_VALUE;
	static int[] result;
    
    public int[] solution(int n, int[] info) {
        int[] answer = {};
        int[] arr = {0,1,2,3,4,5,6,7,8,9,10};
		result = new int[11];
		combination(arr,new int[n],0,0,info);
        
		if(max<0)
			return new int[]{-1};
		else
			return result;
    }
    private static void copy(int[] point) {
		for(int i=0;i<11;i++)
			result[i] = point[i];
	}
    private static void combination(int[] arr, int[] sel, int k,int idx,int[] info)
    {
        if(k == sel.length)
		{
			
			int sum=0;
			int apeach=0;
			
			int[] point = {0,0,0,0,0,0,0,0,0,0,0};
			for(int i=0;i<k;i++)
			{
				point[10-sel[i]]++;
			}
			for(int i=0;i<11;i++)
			{
				if(point[i]>info[i])
					sum = sum + (10-i);
				else if(point[i]<=info[i] && info[i]!=0)
					apeach = apeach + (10-i);
			}
			if(max<sum-apeach && sum-apeach!=0)
			{
				max = sum-apeach;
				copy(point);
				
			}
			return;
		}
		
		for(int i=idx;i<arr.length;i++)
		{
			sel[k] = arr[i];
			combination(arr,sel,k+1,i,info);
		}
	}
}
