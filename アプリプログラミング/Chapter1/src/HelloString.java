import java.util.Scanner;

public class HelloString {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("名前> ");
        String name = stdIn.next();

        System.out.print(name + "さん、こんにちは!");
    }
}
