import java.util.*;

public class EqDist {
    public static void main (String[] args) {
        Solution test=new Solution();
        System.out.println(test);
    }
}
class Solution {
    private ArrayList<Integer> answer;
    private ArrayList<Pair> visited[];
    private Queue<Pair> queue;
    private Map<Integer,ArrayList<Integer>> listInc;
    public Solution() {
        Scanner scan=new Scanner(System.in);
        int N=scan.nextInt();
        int M=scan.nextInt();
        listInc=new HashMap<>();
        queue=new LinkedList<>();
        visited =new ArrayList[N];
        for(int i=0; i<N; i++) visited[i]=new ArrayList<>();
        for(int i=0; i<M; i++) {
            int u=scan.nextInt(), v=scan.nextInt();
            connect(u,v);
            connect(v,u);
        }
        int K=scan.nextInt();
        for(int i=0; i<K; i++) {
            int u=scan.nextInt();
            visited[u].add(new Pair(i, 0));
            queue.clear();
            for(int j=0; j<listInc.get(u).size(); j++) {
                queue.add(new Pair(listInc.get(u).get(j),1));
            }
            BFS(i);
        }
        answer=new ArrayList<>();
        for (int u=0; u<N; u++) {
            if(visited[u].size()==K) {
                int dist=visited[u].get(0).cdr();
                int equal=1;
                for(int j=1; j<visited[u].size(); j++) {
                    if(visited[u].get(j).cdr()!=dist) {
                        equal=0;
                        break;
                    }
                }
                if(equal==1) answer.add(u);
            }
        }
    }
    private void BFS(int step) {
        while (!queue.isEmpty()) {
            Pair elem=queue.remove();
            if (visited[elem.car()].size()!=step) continue;
            visited[elem.car()].add(new Pair(step, elem.cdr()));
            Iterator<Integer> iter = listInc.get(elem.car()).iterator();
            while (iter.hasNext()) {
                int k=iter.next();
                if (visited[k].size() == step) queue.add(new Pair(k, elem.cdr()+1));
            }
        }
    }
    public String toString() {
        String ans="";
        for (int i=0; i< answer.size(); i++) {
            ans+=answer.get(i) +" ";
        }
        if (ans=="") ans="-";
        return ans;
    }
    private void connect(int u, int v) {
        if (listInc.containsKey(u)) {
            if (!listInc.get(u).contains(v)) {
                listInc.get(u).add(v);
            }
        }
        else {
            ArrayList<Integer> values=new ArrayList<>();
            values.add(v);
            listInc.put(u,values);
        }
    }
}
class Pair {
    private int x;
    private int y;
    Pair(int x, int y) {
        this.x=x;
        this.y=y;
    }
    public int car() {return x;}
    public int cdr() {return y;}
}
