class animalBaseClass:
    animallegs = 4
    def walk(self):
        print('あるく')
    def cry(self):
        print('なく')
    def getLegsNum(self):
        print(self.animallegs)

class dogClass(animalBaseClass):
    def __init__(self):
        print('いぬです')

wanko = dogClass()

wanko.walk()
wanko.cry()
wanko.getLegsNum()


class animalBaseClass:
    animallegs = 4
    def walk(self):
        print('あるく')
    def cry(self):
        print('なく')
    def getLegsNum(self):
        print(self.animallegs)

class catClass(animalBaseClass):
    def __init__(self):
        print('ねこです')
    def cry(self):
        print('にゃー')

chachamaru = catClass()
chachamaru.walk()
chachamaru.cry()


class animalBaseClass:
    def __init__(self, num):
        self.animallegs = num
    def walk(self):
        print('あるく')
    def cry(self):
        print('なく')
    def getLegsNum(self):
        print(self.animallegs)

class snakeClass(animalBaseClass):
    def __init__(self, num):
        super().__init__(num)   #super()は子クラスから親クラスのメソッドを呼ぶことができるキーワード
        print('へびです')

nyaro = snakeClass(0)
nyaro.getLegsNum()


import calendar
print(calendar.month(2022,7))


import calendar as cal
print(cal.month(2022,8))


from calendar import month, isleap
print(month(2022,9))
print(isleap(2024))


from datetime import date
print(date.today())


from datetime import date
today = date.today()
print(today.strftime('%Y%m%d'))
print(today.strftime('%y/%m/%d'))
print(today.strftime('%Y年%m月%d日'))
print(today.strftime('%Y %B %d %a'))


from datetime import datetime
print(datetime.now())


from datetime import datetime as dt
now = dt.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))


from datetime import date, timedelta
today = date.today()
print(today)

one_week = timedelta(days = 7)
print(today + one_week)
print(today - one_week)
