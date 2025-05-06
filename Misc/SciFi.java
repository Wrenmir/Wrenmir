import java.util.Scanner;

public class SciFi {
    public static void main(String[] args) {
        /*
         * Take in the following info from the user
         * First name
         * Last name
         * City they are from
         * School they are going to attend after high school
         * City would like to live in
         * Favorite pets name or favorite appetizer
         * Favorite siblings name; if no siblings then favorite mythical character
         * 
         * Print out the info in a nice organized chart like this
         *          first: Bob
         *          last: bob
         *          city: boonville 
         *          school: mcdonalds career academy
         *          pet: mini corndogs
         *          sibling: bobby
         */
        

         System.out.println("What's your first name? ");
         Scanner ui = new Scanner(System.in);
         String first = ui.nextLine();

         System.out.println("What's your last name? ");
         String last = ui.nextLine();

         System.out.println("What city are you from? ");
         String cityFrom = ui.nextLine();

         System.out.println("What school are you attending after high school? ");
         String school = ui.nextLine();

         System.out.println("What city would you like to live in? ");
         String cityToLiveIn = ui.nextLine();

         System.out.println("What's the name of your favorite pet? If you don't have a pet, what's your favorite appetizer? ");
         String petAppetizer = ui.nextLine();

         System.out.println("What's the name of your favorite sibling? If you don't have any siblings, what's your favorite mythical character? ");
         String siblingCharacter = ui.nextLine();

         //System.out.println("\tfirst: "+first+"\n\tlast: "+last+"\n\tcity: "+cityFrom+"\n\tschool: "+school+"\n\tcity to live in: "+cityToLiveIn+"\n\tpet/appetizer: "+petAppetizer+"\n\tsibling/character: "+siblingCharacer);
         
         // how long of a username do we have
        //int userLength = username.length();
        //System.out.println("Your username is %n characters long\n", userLength);

         /*rev 2
         SciFiFirstName = first two letters of FirstName and last two letters of LastName
         SciFiLastName = first 4 letters of city and last 3 letters of school
         SciFiOrigin = first 3 letters of pet and last 3 letters of sibling

         print out -> Howdy SciFiFIrstName SciFiFIrstName from SciFiOrigin!
          */

        String firstA = first.substring(0,3);
        String firstB = last.substring(last.length() - 3);
        

        String lastA = cityFrom.substring(0,5);
        String lastB = school.substring(school.length() - 3);

        String originA = petAppetizer.substring(0,3);
        String originB = siblingCharacter.substring(siblingCharacter.length() - 3);
        

        System.out.println("Howdy "+firstA+firstB+" "+lastA+lastB+" from "+originA+originB);
    }
}
