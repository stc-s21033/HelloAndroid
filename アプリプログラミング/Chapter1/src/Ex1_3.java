import java.util.Scanner;

public class Ex1_3 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.print("姓> "); String lastname = stdIn.next();
        System.out.print("名> "); String firstname = stdIn.next();
        System.out.print("年> "); int year = stdIn.nextInt();
        System.out.print("月> "); int month = stdIn.nextInt();
        System.out.print("日> "); int day = stdIn.nextInt();

        System.out.println(lastname + firstname + "さんは、"+ year + "年" + month + "月" + day + "日生まれです");
    }
}
