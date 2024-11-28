// class HolaMundo {
//     public static void main(String[] args) {

//         int num = 15;
//         System.out.println("this is your number = " + num);
//     }
// }


//SOLUCION CASO PRACTICO 1
// INPUT INTEGER, FLOAT, STRING
// import java.util.Scanner;
// class CasoPractico1 {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
// // getting variables
//         System.out.print("Please write the first number: ");
//         int a = input.nextInt();
        
//         System.out.print("Please write the second number: ");
//         int b = input.nextInt();
        
//         System.out.print("Please write the third number: ");
//         float c = input.nextFloat();

//         input.nextLine();

//         System.out.print("Please write text 1: ");
//         String d = input.nextLine();

//         System.out.print("Please write text 2: ");
//         String e = input.nextLine();

//         // Print the values
//         System.out.println ("the sum of the first 3 numbers is: " + (a+b+c));

//         // conditions to know the biggest number
//         if (a > b && a > c) {
//             System.out.println("the biggest number is: " + a);
//         }
//         else if (b > a && b > c) {
//             System.out.println("the biggest number is: " + b);
//         }
//         else if (c > a && c > b) {
//             System.out.println("the biggest number is: " + c);
//         }

//         // Division among float and Ints
//         float div1 = a / c;
//         float div2 = b / c;

//         System.out.println("First division among " + a + " and " + c + "= " + div1);
//         System.out.println("First division among " + b + " and " + c + "= " + div2);

//         //Concatenation of String lines
//         System.out.println("first text plus second = " + d + " " + e);


//         input.close();
//     }
// }

// SOLUCION CASO PRACTICO 2
// RANDOM NUMBER

// import java.util.Scanner;
// import java.util.Random;
// class CasoPractico2{
//     public static void main(String[] args){
//         Scanner input = new Scanner(System.in);
//         Random random =new Random();

//         System.out.println("Please write how many numbers do you want in the following random print list: ");
//         int num = input.nextInt();


//         int i = 1;
//         while (i <= num){
//             int randomInt = random.nextInt(65 - 18 + 1) + 18;
//             System.out.println("This is your "+i+" random number between 18 and 65: " + randomInt);
//             i ++;
//         }
//         input.close();
//     }
// }

// SOLUCION CASO PRACTICO 3
// RANDOM NUMBER

// import java.util.Scanner;

// class CasoPractico3{
//     public static void main(String[] args){
//     Scanner input = new Scanner(System.in);

//     char letras[] = { 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P',
//     'D', 'X', 'B', 'N', 'J', 'Z', 'S','Q','V', 'H', 'L', 'C', 'K', 'E' };

//     // int dni [];
//     System.out.println("Type your DNI number: ");
//     int num = input.nextInt();
//     int size = String.valueOf(num).length();

//     if (size == 8){
//         System.out.println("This is your number: " + num + " and size: " + size);
//         int mod = num % 23;
//         char letter = letras[mod];
//         System.out.println("This is your number: " + num + letter);
//     }

//     else{
//     System.out.println("This is not a valid number...");
//     }

//     }
// }

// class OperadorTernario{
//         public static void main(String[] args){

// // int numero = 5;
// // se asigna el String para imprimir un mensaje, se pone el igual y posterior la CONDICION 
// // que debe seguir y finalmente se pone el "?" para indicar que debe pasar en caso de ser
// // TRUE, ":" para decir ó FALSO lo que debe pasar en caso contrario...
// // String resultado = (numero % 2 == 0) ? "Es par" : "Es impar";
// // System.out.println(resultado);

//     }
// }