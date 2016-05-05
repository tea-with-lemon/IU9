import java.util.*;


public class Kruskal {
    public static void main(String[] args) {
        RoadBuilder test=new RoadBuilder();
        test.MST();
        System.out.printf("%.2f", test.getWeight());
    }
}
class RoadBuilder{
    private ArrayList<Triplet> edges;
    private ArrayList<Pair> coordinates;
    private int[] groups;
    private double weight;
    public RoadBuilder(){
        coordinates=new ArrayList<>();
        edges=new ArrayList<>();
        Scanner scanner=new Scanner(System.in);
        int N=scanner.nextInt();
        groups=new int[N];
        for (int i=0; i<N;i++) {
            groups[i]=i;
            int x=scanner.nextInt(), y=scanner.nextInt();
            coordinates.add(new Pair(x,y));
        }
        for (int i=0; i<N; i++) {
            for (int j=i+1; j<N; j++) {
                edges.add(new Triplet(i,j,dist(i,j)));
            }
        }
        Collections.sort(edges, new Comparator<Triplet> () {
            @Override
            public int compare(Triplet o1, Triplet o2) {
                if (o1.cddr()>o2.cddr()) return 1;
                else if (o1.cddr()<o2.cddr()) return -1;
                else return 0;
            }
        });
    }
    public Double getWeight() {
        return weight;
    }
    public void MST() {
        int counter=0;
        int e=0;
        weight=(double)0;
        while (counter<groups.length-1) {
            int u1, u2;
            u1=edges.get(e).car();
            u2=edges.get(e).cadr();
            if(groups[u1]!=groups[u2]) {
                int mem=groups[u2];
                counter+=1;
                weight+=edges.get(e).cddr();
                for(int i=0; i<groups.length; i++) if (groups[i]==mem) groups[i]=groups[u1];
            }
            e+=1;
        }
    }
    private Double dist(Integer v1, Integer v2) {
        return Math.sqrt((coordinates.get(v1).car()-coordinates.get(v2).car())*(coordinates.get(v1).car()-coordinates.get(v2).car())+(coordinates.get(v1).cdr()-coordinates.get(v2).cdr())*(coordinates.get(v1).cdr()-coordinates.get(v2).cdr()));
    }
}
class Triplet {
    private int x;
    private int y;
    private double z;
    Triplet(int x, int y, double z) {
        this.x=x;
        this.y=y;
        this.z=z;
    }
    public int car() {return x;}
    public int cadr() {return y;}
    public double cddr() {return z;}
}
class Pair {
    private int x;
    private int y;
    Pair (int x, int y) {
        this.x=x;
        this.y=y;
    }
    public int car() {return x;}
    public int cdr() {return y;}
}

