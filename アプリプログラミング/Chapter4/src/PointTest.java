public class PointTest {
    public static void main(String[] args) {
        Point p1 = new Point(3,5);  //インスタンス(実態)の生成
        Point p2 = new Point(7,8);
        Point p3 = new Point(p2);
        //具体的な2次元座標pointを生成

        //point.x = 3;    //メンバxへの値を代入
        //point.y = 5;    //メンバyへの値を代入

        System.out.println("座標P1(" + p1.getX() + "," + p1.getY() + ")");
        System.out.println("座標P2(" + p2.getX() + "," + p2.getY() + ")");
        System.out.println("2点間の距離: " + p1.distance(p2));
        System.out.println("座標P3(" + p3.getX() + "," + p3.getY() + ")");

    }
}
