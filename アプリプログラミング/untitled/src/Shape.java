import java.awt.*;

/*
    図形
    抽象クラス：抽象メソッドを持ったクラス
 */
public abstract class Shape {
    private Color color;

    //コンストラクタ
    Shape(Color color){
        this.color = color;
    }

    //面積(抽象メソッド)
    public abstract int getArea();

    //アクセサ
    public Color getColor(){return color;}
    public void setColor(Color color){this.color = color;}
}
