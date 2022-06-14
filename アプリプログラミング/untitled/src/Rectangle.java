import java.awt.*;

/*
    矩形
 */

public class Rectangle {
    int width,height;

    //コンストラクタ
    public Rectangle(int width, int height, Color color){
        super(color);    //スーパークラスのコンストラクタ呼び出し
        this.width = width;
        this.height = height;
    }
    //面積
    public int getArea(){
        return width * height;
    }

    //アクセサ
    public int getWidth(){return width;}
    public void setWidth(int width){this.width = width;}
    public int getHeight(){return height;}
    public void setHeight(int height){this.height = height;}
}
