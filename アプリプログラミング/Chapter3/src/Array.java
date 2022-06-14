public class Array {
    public static void main(String[] args) {
        int[] a;    //配列の宣言
        int[] b = {11, 12, 13, 14, 15, 16};    //初期化

        a = new int[5];     //整数5個分の配列オブジェクトを生成
        a[0] = 1;
        a[1] = 2;
        a[2] = 3;
        a[3] = 4;
        a[4] = 5;

        for (int i = 0; i < a.length; i++) {         //配列オブジェクトaは要素数lengthを持つ
            System.out.println("a[" + i + "] = " + a[i]);
        }

        for (int i = 0; i < b.length; i++) {
            System.out.println("b[" + i + "] = " + b[i]);
        }

    }
}
