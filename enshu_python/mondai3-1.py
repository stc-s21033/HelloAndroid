#数字を入力するとその月の英語を表示するプログラムを作成する。
activities = {
    '1':'January',
    '2':'February',
    '3':'March',
    '4':'April',
    '5':'May',
    '6':'June',
    '7':'July',
    '8':'August',
    '9':'September',
    '10':'October',
    '11':'November',
    '12':'December'
}
month = input('何月の単語が知りたいですか？: ')
print(activities[month])
