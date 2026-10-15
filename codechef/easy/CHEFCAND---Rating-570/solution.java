import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
        
        if (sc.hasNextInt()) {
            int T = sc.nextInt();
            
            while (T-- > 0) {
                int n = sc.nextInt();
                int x = sc.nextInt();
                
                if (n <= x) {
                    System.out.println(0);
                } else {
                    int candiesNeeded = n - x;
                    int packetsNeeded = (candiesNeeded + 3) / 4;
                    System.out.println(packetsNeeded);
                }
            }
        }
        sc.close();

	}
}
