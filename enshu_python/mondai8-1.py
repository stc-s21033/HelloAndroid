class pen:
    def write(self):
        print('文字が書ける')
    def shape(self):
        print('長細い形をしている')

class pencil(pen):
    def color(self):
        print('黒色など')
    def eraser(self):
        print('書いた文字が消せる')

class red_pen(pen):
    def color(self):
        print('赤色')

my_pen = red_pen()  #red_penクラスをインスタンス化する
my_pen.write()
my_pen.shape()
my_pen.color()
