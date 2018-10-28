import java.util.*;

public class Dividers {
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        long n=scan.nextLong();
        Solution test=new Solution(n);
        test.builder(n);
        System.out.println(test);
    }
}

class Solution {
    private ArrayList<Long> array = new ArrayList<>();
    private Map<Long,ArrayList<Long>> listInc=new HashMap<>();
    public Solution(long n) {
        array.add((long) 1);
        long d=2;
        long stop= (long) Math.sqrt(n)+1;
        while ((n!= 1)&&(d<=stop)) {
            if (n%d==0) array.add(d);
            while (n%d==0) {
                n=n/d;
            }
            d++;
        }
        if (n!=1) array.add(n);
    }

    private void connect(long u, long v) {
        if (listInc.containsKey(u)) {
            if (!listInc.get(u).contains(v)) {
                listInc.get(u).add(v);
            }
        }
        else {
            ArrayList<Long> values=new ArrayList<>();
            values.add(v);
            listInc.put(u,values);
        }
    }

    public void builder(long n) {
        for (int i=1; i<array.size(); i++) {
            if (n%array.get(i)==0) {
                connect(n,n/array.get(i));
                if (!listInc.containsKey(n/array.get(i))) builder(n/array.get(i));
            }
        }
    }
    public String toString() {
        String ans="graph { \n";
        for (long key : listInc.keySet()) {
            for (long vertex: listInc.get(key)){
                ans+=key + " -- "+vertex+"\n";
            }
        }
        ans=ans+"1\n}";
        return ans;
    }
}
