import java.util.Scanner;

/**
 * 整数の合計
 */
public class DoWhileTest {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int a,sum = 0;
        String str;

        System.out.println("整数の合計を求めます、整数を入力してください");
        do {
            System.out.print("整数> ");
            a = stdIn.nextInt();
            sum += a;

            System.out.print("続けますか？(y/n) > ");
            str = stdIn.next();
        }while(str.equals("y"));

        System.out.println("合計: " + sum);
    }
}
