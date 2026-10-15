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
                int X = sc.nextInt();
                int Y = sc.nextInt();
                
                int maxPeople = X / (2 * Y);
                System.out.println(maxPeople);
            }
        }
        sc.close();

	}
}