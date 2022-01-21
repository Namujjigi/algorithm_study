package BaekJun;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Game {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		long X = Long.parseLong(s[0]);
		long Y = Long.parseLong(s[1]);
		int Z = (int) (Y*100/X);
		
//		System.out.println(Z);
		if(Z>=99)
			System.out.println("-1");
		else
		{
			int result = (int) Math.ceil((100*Y-X*(Z+1))/(double)(Z-99));
			System.out.println(result);
		}
	}


}
