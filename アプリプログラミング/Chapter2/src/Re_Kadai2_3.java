public class Re_Kadai2_3 {
    public static void main(String[] args) {
        for(int i=1; i<=30; i++){
            switch (i%15){
                case 0:
                    System.out.print("@ ");
                    break;
                case 3:
                case 6:
                case 9:
                case 12:
                    System.out.print("* ");
                    break;
                case 5:
                case 10:
                    System.out.print("+ ");
                    break;
                default:
                    System.out.print(i + " ");
                    break;

            }
        }
    }
}
