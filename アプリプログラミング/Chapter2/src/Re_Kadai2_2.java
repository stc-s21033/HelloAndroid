import java.util.Scanner;

public class Re_Kadai2_2 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("時間(秒数): ");
        int time = stdIn.nextInt();

        int h = time/(60*60);
        int m = time%(60*60)/60;
        int s = time%60;
        System.out.printf("%02d:%02d:%02d",h,m,s);
    }
}
