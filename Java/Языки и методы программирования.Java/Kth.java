import java.util.Scanner;

public class Kth
{
    public static void main (String[] args)
    {
        Scanner in=new Scanner (System.in);
        long k=in.nextLong();
        long i, c=9, d;
        for (i=1; i*c <= k; i++)
        {
            k=k-i*c;
            c=c*10;
        }
        d=(long)Math.pow(10, i-k%i-1);
        long n = ((k/i + c/9)/d)%10;
        System.out.println(n);
    }
}
