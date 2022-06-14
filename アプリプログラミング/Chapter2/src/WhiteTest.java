import java.util.Scanner;

/**
 * n個の整数の合計を求める
 */
public class WhiteTest {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n,i=0;
        int a,sum=0;

        System.out.print("入力個数> ");
        n = stdIn.nextInt();

        while (i<n){
            System.out.print("整数> ");
            a = stdIn.nextInt();
            sum += a;
            i++;
        }
        System.out.println("合計: " + sum);
    }
}
