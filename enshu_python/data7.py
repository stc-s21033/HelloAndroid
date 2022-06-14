#class_test

#オブジェクト　クラス
class fruit:
    color = 'red'               #変数
    def taste(self):
        return 'delicious'

apple = fruit()                 #インスタンス化
print(apple.color)
print(apple.taste())

#オブジェクト　文字列
color = 'green'
print(color.count('e'))

#クラスのメソッド引数self
class staff:
    def salary(self):
       return '10000yen'

yamamoto = staff()
print(yamamoto.salary())


class staff:
    bonus = 30000
    def salary(self):
        salary = 10000 + self.bonus
        return salary
yamamoto = staff()
print(yamamoto.salary())

#__init__メソッド （ダンダーイニット）            インスタンスを確実に適切に初期化するための特別なメソッド
class staff:
    def __init__(self,bonus):
        self.bonus = bonus
    def salary(self):
        salary = 10000 + self.bonus
        return salary
yamamoto = staff(50000)
print(yamamoto.salary())
