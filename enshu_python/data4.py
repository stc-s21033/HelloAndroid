#age_str = input('何歳ですか？：')
#age = int(age_str)
#if (60 <= age):
#    print('チケットは1000円です')
#elif (18 <= age):
#    print('チケットは1800円です')
#else:
#    print('チケットを売ることはできません')

#if分の入れ子
pointcard = True
count = 5
if(pointcard == True):
    if(count == 5):
        print('いつもありがとうございます。今回は1000円です')

#1文で複数の条件を表す
pointcard = True
count = 5
if ((pointcard == True) and (count == 5)):
        print('いつもありがとうございます。今回は1000円です')

#for文
for count in range(1,10,2):     #range(開始,終了,増分)
    print('繰り返します')
    print(count)

#f-stringによる文字列の生成              f-string → 文字列の中に任にの値を差し込んで文字列を生成
name = 'グイド'
age = 64
text = f'名前は{name}です。年齢は{age}歳です。'
print(text)

text2 = f'来年は{age+1}歳になります。'
print(text2)
print('来年は',age + 1,'歳になります。')
