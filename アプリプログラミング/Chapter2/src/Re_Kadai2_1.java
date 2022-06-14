import java.util.Scanner;

public class Re_Kadai2_1 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        int n = stdIn.nextInt();

        int i=1;
        while(n>0){
            if((n%10)%2==1)
                System.out.println(i+"桁目は奇数です");
            else
                System.out.println(i+"桁目は偶数です");

            n /= 10;
            i++;
        }
    }
}
