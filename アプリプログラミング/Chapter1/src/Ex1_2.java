import java.util.Scanner;

public class Ex1_2 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        final double pi = 3.14159265;

        System.out.print("半径> ");
        double r = stdIn.nextDouble();

        System.out.println("円の円周の長さ " + ((r*2)*pi));
        System.out.println("円の面積" + pi*r*r);
    }
}
