import java.util.*;

public class MaxNum {
    public static void main(String[] args) {
        Numbers test=new Numbers();
        System.out.println(test);
    }
}
class Numbers {
    ArrayList<Integer> numbers;
    public Numbers() {
        Scanner scan=new Scanner(System.in);
        int N=scan.nextInt();
        numbers=new ArrayList<>(N);
        for (int i=0; i<N; i++) {
            numbers.add(scan.nextInt());
        }
    }
    public String toString() {
        String answer="";
        Collections.sort(numbers, new Comparator<Integer>() {
            @Override
            public int compare(Integer x, Integer y) {
                return -((String.valueOf(x)+String.valueOf(y)).compareTo(String.valueOf(y)+String.valueOf(x)));
            }
        });
        for (int i=0; i<numbers.size(); i++) {
            answer+=numbers.get(i);
        }
        return answer;
    }
}

