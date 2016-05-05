import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class MaxComponent {
    public static void main(String[] args) {
        Finding test=new Finding();
        test.maxComp();
    }
}

class Finding {
    private Map<Integer, ArrayList<Integer>> listInc;
    private boolean[] visited;
    int[] group;
    int edges;
    int vertexes;
    public Finding() {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        visited=new boolean[N];
        group=new int[N];
        int M = scan.nextInt();
        listInc = new HashMap<>();
        for (int i = 0; i < M; i++) {
            int u = scan.nextInt(), v = scan.nextInt();
            if (u != v) connect(u, v);
            connect(v, u);
        }
    }
    private void connect(int u, int v) {
        if (listInc.containsKey(u)) {
            listInc.get(u).add(v);
        } else {
            ArrayList<Integer> values = new ArrayList<>();
            values.add(v);
            listInc.put(u, values);
        }
    }
    private void DFS(int v, int g) {
        group[v]=g;
        visited[v]=true;
        if (listInc.containsKey(v)) {
            edges+=listInc.get(v).size();
            vertexes+=1;
            for (int i = 0; i < listInc.get(v).size(); i++)
                if (!visited[listInc.get(v).get(i)]) DFS(listInc.get(v).get(i), g);
        }
    }
    public void maxComp() {
        int maxVertexes=0;
        int maxEdges=0;
        int numMaxComp=0;
        for (int i=0; i<group.length; i++) {
            if (!visited[i]) {
                edges=0;
                vertexes=0;
                DFS(i, i);
                if (vertexes>maxVertexes || (vertexes==maxVertexes && edges>maxEdges)) {
                    numMaxComp=i;
                    maxVertexes=vertexes;
                    maxEdges=edges;
                }
            }
        }
        System.out.println("graph {");
        for (int v=0; v<group.length; v++) {
            if (group[v]==numMaxComp) {System.out.println(v+"      [color = red]");}
            else System.out.println(v);
            if (listInc.containsKey(v)) {
                for (int u=0; u<listInc.get(v).size(); u++) {
                    if (v < listInc.get(v).get(u)) continue;
                    if (group[listInc.get(v).get(u)]==numMaxComp)
                        System.out.println(listInc.get(v).get(u)+" -- "+v+" [color = red]");
                    else System.out.println(listInc.get(v).get(u)+" -- "+v);
                }
            }
        }
        System.out.println(" }");
    }
}
