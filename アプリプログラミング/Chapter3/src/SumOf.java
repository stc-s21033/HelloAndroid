import java.util.Scanner;

public class SumOf {

    static int sumOf(int n){
        int sum = 0;
        for(int i=1; i<=n; i++){
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        int n = stdIn.nextInt();
        System.out.println("1から"+ n + "までの合計は、" + sumOf(n) + "です。");
    }
}
