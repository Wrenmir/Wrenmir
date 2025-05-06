public class midPointTable{
    public static void main(String[] args) {
        // Declare the points
        int[][] a = {{0, 0}, {1, 4}, {2, 7}, {3, 9}, {4, 11}};
        int[][] b = {{2, 1}, {4, 2}, {6, 3}, {10, 5}, {12, 7}};

        // Print the table header
        System.out.println("a\tb\tMiddle Point");

        // Iterate over the points and calculate the midpoint
        for (int i = 0; i < a.length; i++) {
            double midX = (a[i][0] + b[i][0]) / 2.0;
            double midY = (a[i][1] + b[i][1]) / 2.0;

            // Print the point and its midpoint
            System.out.printf("(%d, %d)\t(%d, %d)\t(%.1f, %.1f)\n",
                    a[i][0], a[i][1], b[i][0], b[i][1], midX, midY);
        }
    }
}