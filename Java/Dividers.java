import java.util.*;

public class Dividers {
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        Solution test=new Solution(n);
        test.builder(n);
        test.toString();
    }
}

class Solution {
    private ArrayList<Integer> array = new ArrayList<Integer>();
    private int[][] matrix;
    public Solution(int n) {
        array.add(1);
        int d=2;
        int stop=n/2;
        while ((n!= 1)&&(d<=stop)) {
            if (n%d==0) array.add(d);
            while (n%d==0) {
                n=n/d;
            }
            d++;
        }
        if (n!=1) array.add(n);
    }

    public void builder(int n) {
        matrix=new int[array.size()][array.size()];
        for (int i=1; i<array.size(); i++) {
            if (n%array.get(i)==0) {
                matrix[n][n/array.get(i)]=1;
                matrix[n/array.get(i)][n]=1;
                builder(n/array.get(i));
            }
        }
    }
    public String toString() {
        String ans="graph {";
        for (int i=0; i<array.size(); i++) {
            for (int j=i; j<array.size(); j++) {
                if (matrix[i][j]==1) {
                    ans+=ans;
                }
            }
        }
        ans=ans+"}";
        return ans;
    }
}
