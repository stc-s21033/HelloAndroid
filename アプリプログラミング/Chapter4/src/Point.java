/**
 * 2次元座標
 */
public class Point {
    int x;  //x座標
    int y;  //y座標

    //コンストラクタ
    Point(int x,int y){
        this.x = x;
        this.y = y;
    }
    Point(Point p){
        this.x = p.x;
        this.y = p.y;
    }

    //アクセサ
    public void setX(int x) {
        this.x = x;
    }
    public void setY(int y) {
        this.y = y;
    }
    public int getX(){
        return x;
    }
    public int getY(){
        return y;
    }

    //２点の距離を求める
    public double distance(Point p){
        return Math.sqrt((p.getX() - this.x) + (p.getY() - this.y) * (p.getY() - this.y));
    }
}
