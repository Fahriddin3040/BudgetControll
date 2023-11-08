from datetime import datetime

EXPENCE = 1
INCOME = 2
time_now = datetime.now()


class NoteModel:

    def __init__(self) -> None:
        self.expence = []
        self.income = []
        self.path = 'path.txt'
        self.balance = 0.0
        with open(self.path, 'a'):
            pass
        self.get()

    def set(self, reason: str, price: int, mode: int) -> None:
        if mode == EXPENCE:
            self.expence.append(['e', reason, price, time_now.strftime("%d/%m/%y %I:%M")])
        elif mode == INCOME:
            self.income.append(['i', reason, price, time_now.strftime("%d/%m/%y %I:%M")])
            self.set_to_file()

    def get(self) -> None:
        var = []
        with open(self.path, 'r', encoding='utf-8') as file:
            var = file.readlines()
        for i in var:
            if i[0] == 'e':
                self.expence.append(i.replace('\n', '').split('*'))
            elif i[0] == 'i':
                self.income.append(i.replace('\n', '').split('*'))
        self.set_to_file()

    def set_to_file(self) -> None:
        with open(self.path, 'w', encoding='utf-8') as file:
            for i in self.expence:
                file.write(f'{i[0]}*{i[1]}*{i[2]}*{i[3]}\n')
            for i in self.income:
                file.write(f'{i[0]}*{i[1]}*{i[2]}*{i[3]}\n')

    def remove(self, choose: int, mode: int) -> None:
        if mode == EXPENCE:
            del self.expence[choose - 1]
        elif mode == INCOME:
            del self.income[choose - 1]
        self.set_to_file()

    def update(self, mode: int, choose: int, reason, price: str) -> None:
        if mode == EXPENCE:
            self.expence[choose - 1][1] = reason
            self.expence[choose - 1][2] = price
        elif mode == INCOME:
            self.income[choose - 1][1] = reason
            self.income[choose - 1][2] = price
        elif mode == 0:
            return
        else:
            raise IndexError
        self.set_to_file()

    def get_balance(self) -> float:
        for i in self.expence:
            self.balance -= float(i[2])
        for i in self.income:
            self.balance += float(i[2])

    def get_lists(self):
        return self.expence, self.income



