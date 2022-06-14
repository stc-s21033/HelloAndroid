#辞書型
activities = {
    'Monday':'バスケ',
    'Tuesday':'自転車',
    'Wednesday':'軽音',
    'Friday':'水泳',
}
activities['Thursday'] = 'サッカー'     #表に追加
activities['Thursday'] = 'バレー'
#print(activities['Tuesday'])
print(activities.keys())        #keys(左)を一覧表示
print(activities.values())      #values(右)を一覧表示

#ダブル型
flavor_list = ['ミント','チョコ','ストロベリー','バニラ']
flavor_list[0] = 'ラムレーズン'       #ミントをラムレーズンに置き換え
print(flavor_list)

#辞書キーに指定できるデータ
diary = {}
key = ('kamata','08-01')
diary[key] = '70kg'
print(diary)

diary = {}
key = ['nakata','08-01']
#diary[key] = '50kg'
#print(diary)

diary = {}
key = ('kamata','08-03')
diary[key] = '72kg'
key = ('nakata','08-03')
diary[key] = '58kg'
key = ('nakata','08-04')
diary[key] = '53kg'
print(diary['kamata','08-03'])
print(diary['nakata','08-03'])
print(diary['nakata','08-04'])

#集合型
candy = {'delicious','fantastic'}
print(candy)
candy = set('delisious')            #１文字ずつバラバラになる
print(candy)

#バラバラにしたくないとき
flavor = ['apple','peach','soda']
candy = set(flavor)
print(candy)
candy.update(['grape'])
print(candy)

#重複データを削除
music = ['my_love','life','life','good_time']
music_set = set(music)      #リスト型 → 集合型
print(music_set)
music = list(music_set)     #集合型 → リスト型
print(music)

#複数のデータ同士の計算
limited_cd = {'good_day','chocolate','loyalty'}
normal_cd = {'good_day','chocolate'}
print(limited_cd - normal_cd)   #差分をとる
print(limited_cd & normal_cd)   #共通のデータを探す
