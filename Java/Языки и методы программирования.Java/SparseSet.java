import java.util.*;

public class SparseSet<T extends Hintable> extends AbstractSet<T>{
    private int n=0;
    private ArrayList<T> dense=new ArrayList<>();
    public int size(){return n;}
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private int i = 0;
            public T next() {return dense.get(i++);}
            public boolean hasNext() {return i<n;}
            public void remove() {SparseSet.this.remove(dense.get(i-1));}
        };
    }
    public boolean contains(Object x){return ((((T)x).hint()>=0) && (((T)x).hint()<n) && (dense.get(((T)x).hint()) == (T)x));}
    public boolean add(T x){
        if (contains(x)==false){
            dense.add(x);
            x.setHint(n);
            n++;
            return true;
        } else return false;
    }
    public boolean remove(Object x){
        if(contains((T)x)==true){
            n--;
            dense.set(((T)x).hint(), dense.get(n));
            dense.get(n).setHint(((T)x).hint());
            return true;
        }else return false;
    }
    public void clear(){n = 0;}
}
