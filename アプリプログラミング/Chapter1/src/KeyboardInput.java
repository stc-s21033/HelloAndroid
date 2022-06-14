import java.util.Scanner;

public class KeyboardInput {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int a,b;

        System.out.print("整数> ");
        a = stdIn.nextInt();
        System.out.print("整数> ");
        b = stdIn.nextInt();

        System.out.println("加算結果" + (a+b));
    }
}
