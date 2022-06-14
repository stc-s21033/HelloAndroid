class calc:
    def __init__(self,a,b):
        self.a = a;
        self.b = b;
    def add(self):
        add = self.a + self.b
        print(f'加法:{add}')
    def sub(self):
        sub = self.a - self.b
        print(f'減法:{sub}')
    def mul(self):
        mul = self.a * self.b
        print(f'加法:{mul}')
    def div(self):
        div = self.a / self.b
        print(f'加法:{div}')

number1_str = input('1つ目の数字を入力してください : ')
num1 = int(number1_str)
number2_str = input('2つ目の数字を入力してください : ')
num2 = int(number1_str)
yamamoto = calc(num1,num2)
print(yamamoto.add())
print(yamamoto.sub())
print(yamamoto.mul())
print(yamamoto.div())
