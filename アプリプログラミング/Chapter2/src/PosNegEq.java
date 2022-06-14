import java.util.Scanner;

/**
* 正負零の判定
 */
public class PosNegEq {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("整数> ");
        int n = stdIn.nextInt();

        if(n>0){
            System.out.println("正です。");
        }
        else if(n==0){
            System.out.println("0です。");
        }
        else {
            System.out.println("負です。");
        }
    }
}
