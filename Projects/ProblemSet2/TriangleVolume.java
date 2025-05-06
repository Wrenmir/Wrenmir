import java.util.Scanner;

public class TriangleVolume {
    public static void main(String[] args) {

        //Create a scanner
        Scanner input = new Scanner(System.in);
    
        //Receive the length of sides of a triangle.
        System.out.println("Enter lenght of the sides and height of the Equilateral triangle: ");
        double lengthOfSides = input.nextDouble();
            
        //area of triangle.
        double areaOfTriangle = lengthOfSides * lengthOfSides * Math.sqrt(3) / 4;
            
        //volume of triangle.
        double volumeOfTriangle = areaOfTriangle * lengthOfSides;
            
        System.out.println("The triangle has an volume of " + volumeOfTriangle);

    }
}
