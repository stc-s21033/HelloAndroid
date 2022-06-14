import java.util.Scanner;

public class Kadai3_2 {

    static int grade(int[] a,int[] b,int[] c){

        for(int i=0;i<10;i++){
            if((a[i]+b[i])>90){
                c[i] = 5;
            }
            else if((a[i]+b[i])>80){
                c[i] = 4;
            }
            else if((a[i]+b[i])>70){
                c[i] = 3;
            }
            else if((a[i]+b[i])>60){
                c[i] = 2;
            }
            else{
                c[i] = 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        int[] a = {32,34,41,28,40,26,14,46,29,50};
        int[] b = {21,33,45,47,39,41,23,32,47,9};
        int[] c ;

        System.out.print("評価は、" + c[i]);

    }
}
