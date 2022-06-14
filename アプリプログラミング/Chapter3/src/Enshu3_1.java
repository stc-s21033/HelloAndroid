import java.util.Scanner;

public class Enshu3_1 {

    static int min(int a,int b,int c) {
        int min = a;

       if(b<min) min = b;
       if(c<min) min = c;

        return min;
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("整数a> "); int a = stdIn.nextInt();
        System.out.print("整数b> "); int b = stdIn.nextInt();
        System.out.print("整数c> "); int c = stdIn.nextInt();

        System.out.println("一番小さな値は" + min(a,b,c) + "です。");
    }
}
