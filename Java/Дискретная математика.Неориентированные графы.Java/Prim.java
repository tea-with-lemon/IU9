import java.util.*;

public class Prim {
    public static void main(String[] args) {
        LinesBuilder test = new LinesBuilder();
        test.MST();
        System.out.println(test);
    }
}
class LinesBuilder {
    private Map<Integer, ArrayList<Pair<Integer, Integer>>> listInc;
    private Integer weight;
    public LinesBuilder(){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int M = scan.nextInt();
        listInc = new HashMap<>();
        for (int i = 0; i < M; i++) {
            int u = scan.nextInt(), v = scan.nextInt(), len=scan.nextInt();
            connect(u, v, len);
            connect(v, u, len);
        }
    }
    private void connect(int u, int v, int len) {
        if (listInc.containsKey(u)) {
            if (!listInc.get(u).contains(v)) {
                listInc.get(u).add(new Pair(v, len));
            }
        } else {
            ArrayList<Pair<Integer, Integer>> values = new ArrayList<>();
            values.add(new Pair(v, len));
            listInc.put(u, values);
        }
    }
    public void MST() {
        weight=0;
        if (listInc.size()==0) return;
        PriorityQueue<Pair<Integer, Integer>> distance;
        boolean[] visited=new boolean[listInc.size()];
        int[] dist=new int[listInc.size()];
        distance=new PriorityQueue<>(listInc.size(), new Comparator<Pair<Integer,Integer>> () {
            @Override
            public int compare(Pair<Integer, Integer> o1, Pair<Integer, Integer> o2) {
                return o1.cdr()-o2.cdr();
            }
        });
        distance.add(new Pair(0,0));
        dist[0]=0;
        visited[0]=false;
        for (int i=1; i<listInc.size(); i++) {
            dist[i]=(999999999);
            distance.add(new Pair(i,999999999));
            visited[i]=false;
        }
        while (!distance.isEmpty()) {
            Pair<Integer, Integer> v=distance.poll();
            if (visited[v.car()]) continue;
            for (int i=0; i<listInc.get(v.car()).size(); i++) {
                Pair<Integer, Integer> u=listInc.get(v.car()).get(i);
                if (!visited[u.car()] && u.cdr()<dist[u.car()]) {
                    dist[u.car()]=u.cdr();
                    distance.add(new Pair(u.car(), u.cdr()));
                }
            }
            visited[v.car()]=true;
            weight+=v.cdr();
        }
    }
    public String toString() {
        return String.valueOf(weight);
    }
}
class Pair<T1,T2> {
    private T1 x;
    private T2 y;
    Pair(T1 x, T2 y) {
        this.x=x;
        this.y=y;
    }
    public T1 car() {return x;}
    public T2 cdr() {return y;}
    @Override
    public boolean equals(Object x) {
        if (x== null) {
            return false;
        }
        if (getClass() != x.getClass()) {
            return false;
        }
        if ((this.x==((Pair) x).car()) && (this.y==((Pair) x).cdr())) return true;
        else return false;
    }
    public String toString() {
        return String.valueOf(x)+" "+String.valueOf(y);
    }
}

