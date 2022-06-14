height_str = input('身長を入力してください：')
height = int(height_str)
weight_str = input('体重を入力してください：')
weight = int(weight_str)

bmi = weight / ((height * 0.01) * (height * 0.01))

if(18.5 > bmi):
    result = 'やせ型'

elif(18.5 <= bmi < 25):
    result = '標準体重'

else:
    result = '肥満'

text = f'判定結果：{result}'
print(text)
