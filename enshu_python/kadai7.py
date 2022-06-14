class Member:
    def __init__(self,no,name,weight):
        self.no = no
        self.name = name
        self.weight = weight
    def member_print(self):
        print(f'No.{self.no}:{self.name} {self.weight}kg')


yamada = Member(15,'山田太郎',72.7)
yamada.member_print()
sekine = Member(37,'関根信彦',65.3)
sekine.member_print()
