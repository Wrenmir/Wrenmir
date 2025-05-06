// imports
import java.util.Scanner;
import java.util.Random;

// main
public class Bellringer0911 {

    public static void main(String[] args) {
        // generate number
        Random rand = new Random();
        int answer = rand.nextInt(10);

        // get user guess
        Scanner ui = new Scanner(System.in);
        System.out.println("Guess a number between 1 and 10");
        String guess = ui.nextLine();

        // clean data; check for correct input
        if (guess.contains(".")) {
            System.out.println("Only whole numbers please.");
            System.out.println("Guess a number between 1 and 10");
            guess = ui.nextLine();
        }
        else if (guess.isEmpty() || guess.isBlank()) {
            System.out.println("No spaces, please");
            System.out.println("Guess a number between 1 and 10");
            guess = ui.nextLine();
        }
        // the regex loops through each digit to check if NOT 0-9
        else if (guess.matches("[^0-9]+")) {
            System.out.println("No letters please");
            System.out.println("Guess a number between 1 and 10");
            guess = ui.nextLine();
        }
        // main
        else {
            // convert guess String to int
            int guessInt = Integer.parseInt(guess);

            while (guessInt != answer) {
                if (guessInt < answer) {
                    System.out.println("Your guess is too low");
                }
                else if (guessInt > answer) {
                    System.out.println("Your guess is too high");
                }
                guess = ui.nextLine();
                guessInt = Integer.parseInt(guess);
            }
            System.out.println("You got it!");
        }

        

    }
}