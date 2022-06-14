public class SumOfArray {

    static int sumOfArray(int[] a){
        int sum = 0;

        for(int i=0; i<a.length; i++){
            sum += a[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        int[] data = {1,3,6,9,11,15,27,34,77};

        System.out.println("合計: " + sumOfArray(data));
    }
}
