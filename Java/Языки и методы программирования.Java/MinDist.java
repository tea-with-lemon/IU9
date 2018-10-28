import java.util.*;
import static java.lang.Math.abs;

public class MinDist {
    public static void main(String[] args) {
        Distance test=new Distance();
        System.out.print(test.dist());
    }
}
class Distance {
    private String S;
    private char x, y;
    public Distance() {
        Scanner in=new Scanner(System.in);
        S=in.nextLine();
        x=in.next().charAt(0);
        y=in.next().charAt(0);
    }
    public int dist() {
        int posX=S.indexOf(x);
        int posY=S.indexOf(y);
        int minDist=abs(posX-posY);
        for (int i=0; i<S.length(); i++) {
            if (S.charAt(i)==x) posX=i;
            else if (S.charAt(i)==y) posY=i;
            if (minDist> abs(posX-posY)) minDist=abs(posX-posY);
        }
        return minDist-1;
    }
}
