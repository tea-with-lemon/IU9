import java.util.AbstractSet;
import java.util.Iterator;

public class IntSparseSet extends AbstractSet<Integer> {
    private int[] sparse;
    private int[] dense;
    private int n;
    private int high, low;
    public IntSparseSet(int low, int high) {
        n=0;
        this.high=high;
        this.low=low;
        dense=new int[high-low];
        sparse=new int[high-low];
        for (int i=0; i<high-low; i++) {
            sparse[i]=-1;
        }
    }
    @Override
    public Iterator<Integer> iterator() {
        return new Iterator<Integer>() {
            private int index=0;
            @Override
            public boolean hasNext() {
                return index < n;
            }
            @Override
            public Integer next() {
                return dense[index++];
            }
            @Override
            public void remove() {
                IntSparseSet.this.remove(dense[index-1]);
            }
        };
    }
    @Override
    public int size() {
        return n;
    }
    @Override
    public boolean contains(Object o) {
        if (o instanceof Integer) {
            int elem = (int) o;
            if (!(elem < high && elem >= low)) return false;
            else if (sparse[elem-low]==-1) return false;
            else if (sparse[elem-low] < n) return true;
            else return false;
        } else return false;
    }
    @Override
    public boolean add(Integer elem) {
        if (elem<high && elem>=low && !this.contains(elem)) {
            dense[n]=elem;
            sparse[elem-low]=n++;
            return true;
        }else return false;
    }
    @Override
    public boolean remove(Object o) {
        if (o instanceof Integer) {
            int elem=(int) o;
            if (!contains(elem))
                return false;
            n--;
            dense[sparse[elem - low]] = dense[n];
            sparse[dense[n] - low] = sparse[elem - low];
            sparse[elem-low]=-1;
            return true;
        } return false;
    }
    @Override
    public void clear() {
        n=0;
    }
}
