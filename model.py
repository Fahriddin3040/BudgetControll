from datetime import datetime

Expence = 1
Income = 2

time_now = datetime.now()


# time_now.utctime("%d/%m/%y %I:%M")


class Storage:

    def __init__(self) -> None:
        self.expence = []
        self.income = []
        self.balance = 0.0
        self.path = ''

    def set(self, reason: str, price: int, mode: int) -> None:
        if mode == Expence:
            self.expence.append(['e', reason, price, time_now.strftime("%d/%m/%y %I:%M")])
        elif mode == Income:
            self.income.append(['i', reason, price, time_now.strftime("%d/%m/%y %I:%M")])
            self.set_to_file()

    def get(self) -> None:
        exp, inc, var = [], [], []
        with open(self.path, 'r', encoding='utf-8') as file:
            var = file.readlines()
        for i in var:
            if i[0] == 'e':
                exp.append(i.replace('\n', '').split('*'))
            elif i[0] == 'i':
                inc.append(i.replace('\n', '').split('*'))
        self.expence = exp
        self.income = inc

    def set_to_file(self) -> None:
        with open(self.path, 'w'):
            pass
        with open(self.path, 'a', encoding='utf-8') as file:
            for i in self.expence:
                print(f'{i[0]}*{i[1]}*{i[2]}*{i[3]}', file=file)
            for i in self.income:
                print(f'{i[0]}*{i[1]}*{i[2]}*{i[3]}', file=file)

    def remove(self, choose: int, mode: int) -> None:
        if mode == Expence:
            del self.expence[choose - 1]
        elif mode == Income:
            del self.income[choose - 1]
        self.set_to_file()

    def update(self, mode: int, choose: int, reason, price: str) -> None:
        if mode == Expence:
            self.expence[choose - 1][1] = reason
            self.expence[choose - 1][2] = price
        elif mode == Income:
            self.income[choose - 1][1] = reason
            self.income[choose - 1][2] = price
        elif mode == 0:
            return
        else:
            raise IndexError
        self.set_to_file()





