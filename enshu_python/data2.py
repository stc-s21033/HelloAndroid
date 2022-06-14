#複数行の文字列を表す方法
print('''
Sunday
Mondey
Tuesday
''')

#文字列の連結
str_renketu = 'thunder' + 'bolt'
print(str_renketu)

#文字の掛け算
str_kake = 'hunter' * 2
print(str_kake)

#大文字に変換する
text = 'hello'
print(text.upper())

#指定した文字をカウント
word = 'maintenance'
print(word.count('n'))

#論旨型
print(46 < 49)
print(46 > 49)

print(True)

#リスト
list = [57, 'banana', 'apple']
print(list)
print(list[0]+1)
#リストの操作
list.append(88)         #追加
print(list)
list.remove('banana')   #削除
print(list)

Agroup=['kazu','gorou','dai']
print(Agroup)
Agroup.sort()           #昇順
print(Agroup)

#数値の場合
test_result = [87,55,99,50,66,76]
test_result.sort()
print(test_result)

#リストの結合
rainbow_in = ['紫','藍','青','緑']
rainbow_out = ['黄','橙','赤']
rainbow_color = rainbow_in + rainbow_out
print(rainbow_color)

#生まれ年をキーボードから入力
year = input('生まれ年を入力してください : ')
#入力された値を表示
print(year)
