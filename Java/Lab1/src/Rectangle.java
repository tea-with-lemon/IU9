public class Rectangle {
    private Point p, p1, p2, p3;
    public Rectangle(Point p, Point p1, Point p2, Point p3) {
        this.p=p;
        this.p1=p1;
        this.p2=p2;
        this.p3=p3;
    }
    private double length(Point p, Point p1) {
        double x=p.returnX();
        double x1=p1.returnX();
        double y=p.returnY();
        double y1=p1.returnY();
        return Math.sqrt(Math.pow((x-x1), 2) + Math.pow((y-y1), 2));
    }
    public double square() {
        return length(p,p1)* length(p1,p2);
    }
    public String toString() {
        return "("+p+", "+p1+", "+p2+", "+p3+ ")";
    }
}
