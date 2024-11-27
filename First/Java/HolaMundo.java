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

        if (a > b && a > c) {
            System.out.println("the biggest number is: " + a);
        }
        else if (b > a && b > c) {
            System.out.println("the biggest number is: " + b);
        }
        else if (c > a && c > b) {
            System.out.println("the biggest number is: " + c);
        }

        System.out.println ("the sum of the first 3 numbers is: " + (a+b+c));
        System.out.print("first text plus second = " + d + e);
        

        input.close();
    }
}

