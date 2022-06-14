month_dict ={
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}

while(True):
    month_str = input("何月の単語が知りたいですか？：")
    if onth_str =='終了':
        break
    month_int = int(month_str)
    print(month_dict[month_int])
