def washingMachine():
    print('給水します')
    print('洗います')
    print('すすぎます')
    print('脱水します')
    print('乾燥します')

washingMachine()

def washingMachine(mode):
    print('給水します')
    if(mode == 'soft'):
        print('やさしく洗う')
    elif(mode == 'hard'):
        print('激しく洗う')
    else:
        print('ふつうに洗う')

washingMachine('soft')

def area(radius):
    result = radius * radius * 3.14
    return result

small = area(5)
big = area(10)
print(small)
print(big)

#len関数
print(len('thunderbolt'))       #文字数を数える
animal = ['cat','dog','duck']
print(len(animal))              #要素を数える

#max関数　min関数
print(max(100,10,50))       #最大四を返す
print(min(300,30,3000))     #最小値を返す

print(max('thunderbolt'))   #数字 → 大文字英語 → 小文字英語

print(min('1Aa'))
print(max('1Aa'))

#sorted関数       渡したデータを並べ替えて、リスト型で返す
print(sorted('thunderbolt'))
print(sorted('1Aa'))
print(sorted([100,95,55,78,80,78]))

#dir関数
string = 'nikuman'
print(dir(string))

#例外処理の書き方
try:
    prin('例外が発生してしまう処理')
except:
    print('例外をキャッチしました')

#例外処理の対処法
try:
    prin('a')
except Exception as e:
    print(e)
