number_str = input('数字を入力してください')
number = int(number_str)

if number < 10:
    result = '1桁'
elif number < 100:
    result = '2桁'
elif number < 1000:
    result = '3桁'
else:
    result = '4桁以上'

write_file = open('kadai9.txt','w')
text = f'入力された数字は{result}です'
write_file.write(text)
write_file.file()
