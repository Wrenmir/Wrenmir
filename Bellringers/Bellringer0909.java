import java.util.Scanner;
public class Bellringer0909 {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("99 bottles of . . .");
        String whatsInTheBottle = ui.nextLine();
        for(int i=99;i!=0;i--){
            System.out.println("\nKeep going??? Press enter to go one - - ");
            String moveOn = ui.nextLine();
            String verse = i+" bottles of "+whatsInTheBottle+", "+i+" bottles of "+whatsInTheBottle+" Take one down and pass it around . . . ";
            if (moveOn==""){
                System.out.print("\033[H\033[2J");
                System.out.print(verse);
            }
            else{
                System.out.print("You stop at "+i+" bottles");
            }
        }
        System.out.println("\nWOW YOU FINISHED WASTING YOUR TIME");
    }
}