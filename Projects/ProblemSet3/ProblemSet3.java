import java.util.Scanner;
import java.util.Random;

public class ProblemSet3 {
    public static void main(String[] args) {
        //findFutureDates();
        //sortThreeInts();
        //palindromeInteger();
        //rpslsBattle();
        randomCard();
    }
    private static void findFutureDates() {
        Scanner scan1 = new Scanner(System.in);

        // Input for todays day
        System.out.print("Enter today's day of the week (0 for Sunday, 1 for Monday, etc.): ");
        int today = scan1.nextInt();

        // Check for correct input of todays day
        if (today<0 || today>6) {
            System.out.print("Please enter a number between 0 and 6. Enter today's day of the week (0 for Sunday, 1 for Monday, etc.): ");
            today = scan1.nextInt();
        }

        // Input for days after today
        System.out.print("Enter the number of days after today: ");
        int daysAfter = scan1.nextInt();

        // Calculate future day, handling wrap-around
        int futureDay = (today + daysAfter) % 7;
        String todayName = "";
        String futureDayName = "";

        // Method to determine the day name based on the day number ; CREDIT - ChatGPT ... i(wren) had it rewrite jins code to meet the requirements... and rewrote some of chatGPTs code too :)
        if (today == 0) {todayName = "Sunday";} 
        else if (today == 1) {todayName = "Monday";}
        else if (today == 2) {todayName = "Tuesday";}
        else if (today == 3) {todayName = "Wednesday";}
        else if (today == 4) {todayName = "Thursday";}
        else if (today == 5) {todayName = "Friday";}
        else {todayName = "Saturday";}

        if (futureDay == 0) {futureDayName = "Sunday";}
        else if (futureDay == 1) {futureDayName = "Monday";}
        else if (futureDay == 2) {futureDayName = "Tuesday";}
        else if (futureDay == 3) {futureDayName = "Wednesday";}
        else if (futureDay == 4) {futureDayName = "Thursday";}
        else if (futureDay == 5) {futureDayName = "Friday";}
        else {futureDayName = "Saturday";}

        System.out.println("Today is " +todayName+ ". The future day of the week is " +futureDayName+ ".");
    }
    private static void sortThreeInts() {
        Scanner scan2 = new Scanner(System.in);

        // Input for ints
        System.out.print("1st Int: ");
        int num1 = scan2.nextInt();

        System.out.print("2nd Int: ");
        int num2 = scan2.nextInt();

        System.out.print("3rd Int: ");
        int num3 = scan2.nextInt();

        // Sort and print ints
        if (num1 <= num2 && num1 <= num3) {
            if (num2 <= num3) {
                System.out.println(num1 + " " + num2 + " " + num3);
            } else {
                System.out.println(num1 + " " + num3 + " " + num2);
            }
        } else if (num2 <= num1 && num2 <= num3) {
            if (num1 <= num3) {
                System.out.println(num2 + " " + num1 + " " + num3);
            } else {
                System.out.println(num2 + " " + num3 + " " + num1);
            }
        } else {
            if (num1 <= num2) {
                System.out.println(num3 + " " + num1 + " " + num2);
            } else {
                System.out.println(num3 + " " + num2 + " " + num1);
            }
        }
    }
    private static void palindromeInteger() {
        Scanner scan3 = new Scanner(System.in);
        String isPal = "";
        
        // Input for num
        System.out.print("Enter a three-digit number: ");
        int num = scan3.nextInt();

        // Check for correct input
        if (num<100 || num>999){
            System.out.print("Please enter a three-digit number: ");
            num = scan3.nextInt();
        }

        // Extract digits
        int digit1 = num / 100;
        int digit3 = num % 10;

        // Check if they're the same
        if (digit1 == digit3) {
            isPal = "is a palindrome";
        }
        else {
            isPal = "is not a palindrome";
        }

        // Print results
        System.out.print(num + " " + isPal);
    }
    private static void rpslsBattle() {
        // A LOT OF THIS CODE IS CREDITED TO CHATGPT - i(wren) had it rewrite jins code to meet the requirements... i(wren) also rewrote a lot of chatGPTs code and added the too thing :) im so cool
        Scanner scan4 = new Scanner(System.in);
        Random random1 = new Random();
        String playerChoiceStr = "";
        String compChoiceStr = "";
        String result = "";
        String too = "";

        System.out.print("Rock (0), paper (1), scissors (2), lizard (3), or spock (4): ");
        int playerChoice = scan4.nextInt();

        // Validate input (player should only enter 0, 1, 2, 3, or 4)
        if (playerChoice < 0 || playerChoice > 4) {
            System.out.println("Invalid input. Please enter a number between 0 and 4.");
            playerChoice = scan4.nextInt();
        }

        // Computer's choice
        int compChoice = random1.nextInt(5);

        // Figure out what player chose ; convert number to corresponding choice
        if (playerChoice == 0) {playerChoiceStr="rock";}
        else if (playerChoice == 1) {playerChoiceStr="paper";}
        else if (playerChoice == 2) {playerChoiceStr="scissors";}
        else if (playerChoice == 3) {playerChoiceStr="lizard";}
        else {playerChoiceStr="spock";}

        // Figure out what comp chose ; convert number to corresponding choice
        if (compChoice == 0) {compChoiceStr="rock";}
        else if (compChoice == 1) {compChoiceStr="paper";}
        else if (compChoice == 2) {compChoiceStr="scissors";}
        else if (compChoice == 3) {compChoiceStr="lizard";}
        else {compChoiceStr="spock";}

        // Determine results
        if (playerChoice == compChoice){result="It is a draw.";too=" too";}
        else if ((playerChoice == 0 && (compChoice == 2 || compChoice == 3)) ||  // Rock beats scissors and lizard
                 (playerChoice == 1 && (compChoice == 0 || compChoice == 4)) ||  // Paper beats rock and spock
                 (playerChoice == 2 && (compChoice == 1 || compChoice == 3)) ||  // Scissors beats paper and lizard
                 (playerChoice == 3 && (compChoice == 1 || compChoice == 4)) ||  // Lizard beats paper and spock
                 (playerChoice == 4 && (compChoice == 0 || compChoice == 2))) {  // Spock beats rock and scissors
            result="You won.";
        } 
        else {
            result="The computer won.";
        }

        // Print results
        System.out.print("You chose "+playerChoiceStr+". The computer chose "+compChoiceStr+too+". "+result);

    }
    private static void randomCard() {
        // Credit to chatGPT for rewritting jins code again
        Scanner scan5 = new Scanner(System.in);
        Random random2 = new Random();

        // Generate a random number for the suit (0 to 3)
        int suitIndex = random2.nextInt(4);
        String suit = "";
        if (suitIndex == 0) {
            suit = "Hearts";
        } else if (suitIndex == 1) {
            suit = "Diamonds";
        } else if (suitIndex == 2) {
            suit = "Clubs";
        } else if (suitIndex == 3) {
            suit = "Spades";
        }

        // Generate a random number for the rank (0 to 12)
        int rankIndex = random2.nextInt(13);
        String rank = "";
        if (rankIndex == 0) {
            rank = "2";
        } else if (rankIndex == 1) {
            rank = "3";
        } else if (rankIndex == 2) {
            rank = "4";
        } else if (rankIndex == 3) {
            rank = "5";
        } else if (rankIndex == 4) {
            rank = "6";
        } else if (rankIndex == 5) {
            rank = "7";
        } else if (rankIndex == 6) {
            rank = "8";
        } else if (rankIndex == 7) {
            rank = "9";
        } else if (rankIndex == 8) {
            rank = "10";
        } else if (rankIndex == 9) {
            rank = "Jack";
        } else if (rankIndex == 10) {
            rank = "Queen";
        } else if (rankIndex == 11) {
            rank = "King";
        } else if (rankIndex == 12) {
            rank = "Ace";
        }

        // Display the card
        System.out.println("You drew the " + rank + " of " + suit);
    }
}

// Credit to jin for code
// Credit to wren for compiling and rewritting to meet requirements