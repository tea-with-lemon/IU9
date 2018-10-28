import java.util.Scanner;

public class Econom {
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        String s=scanner.nextLine();
        int k=0;
        while (s.indexOf(')')!=-1) {
            int p=s.indexOf(')');
            String expr=s.substring(p-4,p+1);
            s=s.replace(expr, String.valueOf(k));
            k++;
        }
        System.out.println(k);
    }
}

