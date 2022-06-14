public class Kadai4_1 {
    public static void main(String[] args) {
        Triangle t1 = new Triangle(5,6);
        Triangle t2 = new Triangle(12,3);

        System.out.println("三角形1　横:"+ t1.getWidth() +" 高さ:"+ t1.getHeight() +" 面積:"+ t1.getArea());
        System.out.println("三角形2　横:"+ t2.getWidth() +" 高さ:"+ t2.getHeight() +" 面積:"+ t2.getArea());
    }
}
