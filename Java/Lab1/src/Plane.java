public class Plane {
    int numPoints=0;
    Point[] points;
    public Plane(int limit) {
        points = new Point[limit];
    }
    public void newPoint(Point p) {
        if(numPoints == points.length) {
            System.out.println("Limit has been achieved already!");
        }
        else {
            points[numPoints]=p;
            numPoints++;
        }
    }
    public Rectangle newRectangle() {
        if (numPoints ==0){
            System.out.println("There are no points!");
            return new Rectangle(new Point(0,0),new Point(0,0), new Point(0,0), new Point(0,0));
        }
        double minX= points[0].returnX(), minY= points[0].returnY(), maxX=minX, maxY=minY;
        for(int i = 1; i< numPoints; i++) {
            if(points[i].returnX()<minX) {
                minX= points[i].returnX();
            }
            if(points[i].returnY()<minY) {
                minY= points[i].returnY();
            }
            if(points[i].returnX()>maxX) {
                maxX= points[i].returnX();
            }
            if(points[i].returnY()>maxY) {
                maxY= points[i].returnY();
            }
        }
        return new Rectangle(new Point(minX,minY),new Point(minX, maxY), new Point(maxX,maxY), new Point(maxX,minY));
    }
    public String toString() {
        String s="Точек: " + numPoints + "\n";
        for(int i = 0; i< numPoints; i++){
            s+= points[i]+" ";
        }
        return s;
    }

}
