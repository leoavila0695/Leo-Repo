// class HolaMundo {
//     public static void main(String[] args) {

//         int num = 15;
//         System.out.println("this is your number = " + num);
//     }
// }



import java.util.Scanner;
class CasoPractico1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
// getting variables
        System.out.print("Please write the first number: ");
        int a = input.nextInt();
        
        System.out.print("Please write the second number: ");
        int b = input.nextInt();
        
        System.out.print("Please write the third number: ");
        float c = input.nextFloat();

        input.nextLine();

        System.out.print("Please write text 1: ");
        String d = input.nextLine();

        System.out.print("Please write text 2: ");
        String e = input.nextLine();

        // Print the values
        System.out.println ("the sum of the first 3 numbers is: " + (a+b+c));

        // conditions to know the biggest number
        if (a > b && a > c) {
            System.out.println("the biggest number is: " + a);
        }
        else if (b > a && b > c) {
            System.out.println("the biggest number is: " + b);
        }
        else if (c > a && c > b) {
            System.out.println("the biggest number is: " + c);
        }

        // Division among float and Ints
        float div1 = a / c;
        float div2 = b / c;

        System.out.println("First division among " + a + " and " + c + "= " + div1);
        System.out.println("First division among " + b + " and " + c + "= " + div2);

        //Concatenation of String lines
        System.out.println("first text plus second = " + d + " " + e);


        input.close();
    }
}

