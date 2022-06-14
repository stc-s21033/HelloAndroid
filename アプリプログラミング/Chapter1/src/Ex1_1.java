import java.util.Scanner;

public class Ex1_1 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int a,b;

        System.out.print("底辺> ");
        a = stdIn.nextInt();
        System.out.print("高さ> ");
        b = stdIn.nextInt();

        System.out.print("三角形の面積は"+ ((a*b)/2));
    }
}
