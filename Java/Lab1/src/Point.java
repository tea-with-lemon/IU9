public class Point {
    private double x,y;
    public Point(double x, double y) {
        this.x=x;
        this.y=y;
    }
    public double returnX() {
        return x;
    }
    public double returnY() {
        return y;
    }
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}