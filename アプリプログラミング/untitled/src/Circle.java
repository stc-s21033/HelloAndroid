import java.awt.*;

/*
    円
 */

public class Circle {
    private int radius;

    //コンストラクタ
    public Circle(int radius,Color color){
        super(color);   //スーパークラスのコンストラクタ呼び出し
        this.radius = radius;
    }

    //面積
    public int getArea(){
        return (int)(Math.PI * radius * radius);
    }

    //アクセサ

    public int getRadius(){return  radius;}
    public void setRadius(int radius){this.radius = radius;}
}
