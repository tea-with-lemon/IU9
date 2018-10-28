import java.util.Random;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner reader=new Scanner(System.in);
        Random random = new Random();
        int n=reader.nextInt();
        Plane plane =new Plane(n);
        for (int i=0; i<n; i++) {
            plane.newPoint(new Point(random.nextInt(50),random.nextInt(50)));
        }
        System.out.println(plane);
        Rectangle rectangle= plane.newRectangle();
        System.out.println(rectangle);
        System.out.println(rectangle.square());
    }
}