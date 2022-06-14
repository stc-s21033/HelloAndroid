import java.awt.*;

public class ShapeTester {
    public static void main(String[] args) {
        Shape rect = new Rectangle(5,8,Color.Cyan);
        Shape circle = new Circle(7, Color.PINK);

        System.out.println("矩形の面積" + rect.getArea() + "色：" + rect.getColor());
        System.out.println("円の面積" + circle.getArea() + "色：" + circle.getColor());
    }
}
