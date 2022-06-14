##　第三週　課題提出

S21-033　　直木 優

### 1.問題

1. 正の整数nを入力して、その階乗値を求めるプログラムKadai3_1.javaを作成しなさい。ただし、正
   の整数を引数として階乗値n!を戻り値とする関数fact(int n)を定義して利用すること。

2. 10人分の生徒の英語と数学の点数(各50点満点){32,34,41,28,40,26,14,46,29,50}と
   {21,33,45,47,39,41,23,32,47,9}がそれぞれ順番に配列aとbに格納されています。各生徒の合計点を
   求めて、その評価を90以上ならば5を、80以上90未満ならば4を、70以上80未満ならば3を、60以上
   70未満ならば2を、60未満ならば1として配列cに格納し、結果を表示するプログラムKadai3_2.java
   を作成しなさい。ただし、英語の点数が格納された配列aと数学の点数が格納された配列bと評価を
   格納する配列cを引数として、評価を決定する関数grade(int[] a, int[] b, int[] c)を千絵義して利用する
   こと。

3. 整数を入力して、10個の整数{5,7,8,10,13,15,16,19,23,26}の中から二分探索アルゴリズムを使ってそ
   の値が何番目の要素かを戻り値とするメソッドbinarySearch()を定義して、そのあるかを調べるプロ
   グラムを作成しなさい。

###２．ソースコード

プログラム1.
```java
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
```

プログラム2.
```java
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
```

プログラム3.
```java
```

### 3.実行結果
プログラム1.

![実行結果]()

プログラム2.

![実行結果]()

プログラム3.

![実行結果]()

### 4.感想
戻り値がよくわかりませんでした。