import java.util.Scanner;

public class Kadai2_1 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("整数を入力してください> ");
        int n = stdIn.nextInt();

        if(n%2==1) {
            System.out.println("奇数です。");
        }
        else {
            System.out.println("奇数ではありません。");
        }
    }
}
