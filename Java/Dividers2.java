import java.util.ArrayList;
import java.util.Scanner;

public class Dividers2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Div div = new Div(scanner.nextLong());
        div.graph();
    }
}

class Div {
    private long number;
    private ArrayList<Long> masDividers;

    public Div(long n) {
        this.number = n;
        masDividers = new ArrayList <>() ;
        find_dividers();
    }

    public void find_dividers() {
        int k = (int) Math.sqrt(number);
        int i;
        for (i = 1; i < k + 1; i++)
            if (number % i == 0) {
                masDividers.add(number / i);
            }
        int m = masDividers.size();
        for (i = m-1; i>=0; i--)
            if (masDividers.get(i) != k)
                masDividers.add(number / masDividers.get(i));
    }

    public void graph() {
        System.out.println("graph { ");
        for (int i = 0; i < masDividers.size(); i++)
            System.out.println(masDividers.get(i));
        for (int i = 0; i < masDividers.size(); i++) {
            for (int j = i + 1; j < masDividers.size(); j++) {
                if ((masDividers.get(i) % masDividers.get(j)) == 0) {
                    int h = 0;
                    for (int k = i + 1; k < j; k++) {
                        if (masDividers.get(k) % masDividers.get(j) == 0 && masDividers.get(i)% masDividers.get(k)==0) {
                            h++;
                            break;
                        }
                    }
                    if (h == 0) System.out.println(masDividers.get(i) + "--" + masDividers.get(j));
                }
            }
        }
        System.out.println("}");
    }
}
