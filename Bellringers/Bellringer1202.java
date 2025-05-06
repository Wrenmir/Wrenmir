import java.util.Scanner;

public class Bellringer1202 {
    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        System.out.println("1st num: ");
        Double num1 = ui.nextDouble();
        System.out.println("2nd num: ");
        Double num2 = ui.nextDouble();
        
        while(num2==0){
            for(int i=1;i>0;){
                if(i==1){
                    System.out.println("You cannot divide by zero");
                    System.out.print("Second Number: ");
                    num2 = ui.nextDouble();
                    if(num2==0){
                        i++;
                    }
                }
                if(i==2){
                    System.out.println("The program will crash...");
                    System.out.print("Second Number: ");
                    num2 = ui.nextDouble();
                    if(num2==0){
                        i++;
                    }
                }
                if(i==3){
                    System.out.println("Are you sure you want to crash the program?");
                    String response = ui.nextLine();
                    response = ui.nextLine();
                    if(response=="yes"){
                        System.out.println(num1/num2);
                    }
                    else{
                        System.out.print("Second Number: ");
                        num2 = ui.nextDouble();
                        if(num2==0){
                            i++;
                        }
                    }
                }
                if(i==4){
                    System.out.println("okay wise guy...");
                    i=1;
                }
            }
        }
    }
   
}
