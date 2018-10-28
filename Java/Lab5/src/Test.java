import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> f(ArrayList<ArrayList<Integer>> lists) {
        return lists.stream()
                .filter(Objects::nonNull)
                .map(row -> row.stream()
                        .mapToInt(x -> x)
                        .min().getAsInt())
                .collect(Collectors.toList());
    }
}

public class Test {

    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> mins= new ArrayList<>();
        Random random=new Random();
        for (int i=0; i<10; i++) {
            ArrayList<Integer> a = new ArrayList<>();
            for (int j=0; j<3; j++) a.add(random.nextInt(10));
            System.out.println(a);
            mins.add(a);
        }
        Solution s = new Solution();
        System.out.println(s.f(mins));


    }
}
