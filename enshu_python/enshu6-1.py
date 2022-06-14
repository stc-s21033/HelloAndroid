#西暦を入力して、和暦を返すプログラムを作成せよ。ただし、関数に引数を渡して
#返り値を受け取る形で実行すること。また、例外処理を実行すること

def age(year2):
    if(year2<=1988):
        print('平成より前です')

    elif((1989<=year2) and (year2<=2018)):
        text = f'平成{year - 1988}年です'
        print(text)

    elif(2019<=year2):
        text = f'令和{year - 2018}年です。'
        print(text)

    else:
        try:
            prin('例外が発生してしまう処理')
        except:
            print('例外をキャッチしました')

year_str = input('西暦を入力してください：')
year = int(year_str)

result = age(year)
