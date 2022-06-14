class Member:
    no = 15;
    name = '山田太郎'
    weight = 72.2
    def member_print(self):
        print(f'No.{self.no}:{self.name} {self.weight}kg')

yamada = Member()
yamada.member_print()
