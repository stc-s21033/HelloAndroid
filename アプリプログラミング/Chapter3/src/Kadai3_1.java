import java.util.Scanner;

public class Kadai3_1 {

    static int fact(int n){

        int sum = 0;

        sum = n * (n-1);

        for(int i=1; i<n; i++){
            sum = sum * (n-(i+1));
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("正の整数を入力してください> ");
        int n = stdIn.nextInt();

        System.out.println("階乗値は、" + fact(n));
    }
}
