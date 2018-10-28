public class Element<T> {
    private T x;
    private Element<T> main;
    private long rank;
    public Element(T x) {
        this.x = x;
        main = this;
        rank = 0;
    }
    public  T x()
    {
        return x;
    }
    private Element<T> findMain() {
        if (main == this) {return main;}
        main = main.findMain();
        return main;
    }
    public Boolean equivalent(Element<T> elem) {
        Element<T> this_main = this.findMain();
        Element<T> elem_main = elem.findMain();
        return (this_main == elem_main);
    }
    public void union(Element<T> elem) {
        Element<T> this_main = this.findMain();
        Element<T> elem_main = elem.findMain();
        if (this_main.rank < elem_main.rank) {
            this_main.main = elem_main;
            return;
        }
        elem_main.main = this_main;
        if ((this_main.rank == elem_main.rank) && (elem_main != this_main)) {
            this_main.rank++;}
    }
}
