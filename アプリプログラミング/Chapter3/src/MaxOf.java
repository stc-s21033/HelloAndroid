import java.util.Scanner;

public class MaxOf {
    //2つの整数のうち大きいほうを求める
    static int max(int a,int b){
        return a>b ? a:b;
    }
    //3つの整数のうち大きいほうを求める     !!同じメソット名を付けることができる
    static int max3(int a,int b,int c) {
        int max;

        max = max(a,b);
        max = max(max,c);

        return max;
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("整数a> "); int a = stdIn.nextInt();
        System.out.print("整数b> "); int b = stdIn.nextInt();
        System.out.print("整数c> "); int c = stdIn.nextInt();

        System.out.println("一番大きな値は" + max3(a,b,c) + "です。");
    }
}
