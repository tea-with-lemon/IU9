import java.util.*;

public class BridgeNum {
    public static void main(String[] args) {
        BridgeSearch test=new BridgeSearch();
        System.out.println(test);
    }
}
class BridgeSearch {
    private Map<Integer, ArrayList<Integer>> listInc;
    private int time=0;
    private int counter=0;
    private int[] enter;
    private int[] exit;

    public BridgeSearch() {
        Scanner scan=new Scanner(System.in);
        int N=scan.nextInt();
        int M=scan.nextInt();
        listInc = new HashMap<>();
        for (int i=0; i<M; i++) {
            int u=scan.nextInt(), v=scan.nextInt();
            connect(u, v);
            connect(v, u);
        }
        enter=new int[listInc.size()];
        exit=new int[listInc.size()];
    }

    private void connect(int u, int v) {
        if (listInc.containsKey(u)) {
            if (!listInc.get(u).contains(v)) {
                listInc.get(u).add(v);
            }
        } else {
            ArrayList<Integer> values=new ArrayList<>();
            values.add(v);
            listInc.put(u, values);
        }
    }

    private void search(int v, int prev) {
        time+=1;
        enter[v]=time;
        exit[v]=time;
        for (int i=0; i<listInc.get(v).size(); i++) {
            int u=listInc.get(v).get(i);
            if (u==prev) continue;
            if (enter[u]==0) {
                search(u, v);
                exit[v]=Math.min(exit[v], exit[u]);
                if (exit[u]>enter[v]) counter+=1;
            } else if (enter[u]<enter[v]) {
                exit[v]=Math.min(exit[v], enter[u]);
            }
        }
    }

    public String toString() {
        for (int i=0; i<listInc.size(); i++) {
            if (enter[i]==0) {
                search(i, i);
            }
        }
        return String.valueOf(counter);
    }
}

