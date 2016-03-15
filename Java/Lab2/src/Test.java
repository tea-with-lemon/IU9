import java.util.Arrays;

public class Test {
    public static void main(String[] args) {
        SeqChar[] chars=new SeqChar[] {
            new SeqChar("Java".toCharArray()),
            new SeqChar("Scala".toCharArray()),
            new SeqChar("Scheme".toCharArray()),
            new SeqChar("Haskell".toCharArray())
        };
        Arrays.sort(chars);
        for (SeqChar elem: chars) System.out.println(elem);

    }
}
