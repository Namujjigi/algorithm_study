package BaekJun;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Contract {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String star_Vega ="(100+1+|01)+";
		for(int i=0;i<N;i++)
		{
			String s = br.readLine();
			if(s.matches(star_Vega))
				System.out.println("YES");
			else
				System.out.println("NO");
		}
	}

}
