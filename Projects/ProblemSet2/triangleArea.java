import java.util.Scanner;

public class triangleArea {

    public static void main(String[] args) {

        Scanner ui = new Scanner(System.in);

        System.out.println("Enter the coordinates of three points separated by spaces like x1 y1 x2 y2 x3 y3: ");
        double x1 = ui.nextDouble();
        double y1 = ui.nextDouble();
        double x2 = ui.nextDouble();
        double y2 = ui.nextDouble();
        double x3 = ui.nextDouble();
        double y3 = ui.nextDouble();

        double area = Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0);

        System.out.println("The area of the triangle is " + area);
    }
}