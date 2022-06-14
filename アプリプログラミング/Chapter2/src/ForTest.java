import java.util.Scanner;

/**
 * 1からnまでの整数の合計
 */
public class ForTest {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int sum = 0;

        System.out.print("入力個数> ");
        int n = stdIn.nextInt();

        for(int i=0; i<n; i++){
            sum += i;
        }
        System.out.println("合計: " + sum);
    }
}
