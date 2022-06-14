rainbow_in = ['紫','藍','青','緑']
rainbow_out = ['黄','橙','赤']
rainbow_color = rainbow_in + rainbow_out
number_str = input('何番目の色が知りたいですか？ : ')
number = int(number_str)        #数値として扱いたい場合は int
print(rainbow_color[number-1])
