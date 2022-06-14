import java.util.Scanner;

public class Test1 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("あなたの名前と身長、体重を入力してください。");
        System.out.print("名前> ");
        String name = stdIn.next();
        System.out.print("身長(cm)> ");
        double cm = stdIn.nextDouble();
        System.out.print("体重(kg)> ");
        double kg = stdIn.nextDouble();

        System.out.println(name + "のBMIは、" + ((kg/(cm*cm))*10000) + "です。");
    }
}
