#ある商品の税抜き価格と個数を入力して、税込みの合計金額を返す
#プログラムを作成しなさい。ただし、必ず関数を使うこと。

def price(money2,number2):
    result = number2 * (money2 + (money2 * 0.1))
    return result

money_str = input('金額(税抜き価格)を入力してください：')
money = int(money_str)
number_str = input('個数を入力してください：')
number = int(number_str)

sum = price(money,number)
text = f'税込み価格は{sum}円です。'
print(text)
