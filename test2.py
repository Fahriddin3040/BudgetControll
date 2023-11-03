from datetime import datetime

global E, I
E = 1
I = 2

time_now = datetime.now()


# time_now.utctime("%d/%m/%y %I:%M")


class Storage:

    def __init__(self) -> None:
        self.expence = []
        self.income = []
        self.balance = 0.0
        self.path = ''

    def set(self, reason: str, price: int, mode: int) -> None:
        if mode == E:
            self.expence.append(['e', reason, price, time_now.strftime("%d/%m/%y %I:%M")])
        elif mode == I:
            self.income.append(['i', reason, price, time_now.strftime("%d/%m/%y %I:%M")])

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

    def remove(self, choose: int, type: int) -> None:
        if type == E:
            del self.expence[choose - 1]
        elif type == I:
            del self.income[choose - 1]

    def update(self, type: int, choose: int, reason, price: str) -> None:
        if type == E:
            self.expence[choose - 1][1] = reason
            self.expence[choose - 1][2] = price
        elif type == I:
            self.income[choose - 1][1] = reason
            self.income[choose - 1][2] = price
        elif type == 0:
            return
        else:
            raise IndexError


class View:

    @staticmethod
    def print_notes(nested_list: list) -> None:
        if type == 1:
            print('\n\tРосходы:')
        elif type == 2:
            print('\n\tДоходы:')
        for i in range(0, len(nested_list)):
            print(f'\t\t{i + 1}.Причина: {nested_list[i][1]} . Сумма: {nested_list[i][2]} . Дата: {nested_list[i][3]}.')
        print()

    @staticmethod
    def show_main_menu() -> None:
        menu = ["1.Добваить росход", "2.Добавить доход", "3.История росходов", "4.История доходов", "5.Баланс",
                "6.Операции", "0.Выход"]
        for i in menu:
            print(i)

    @staticmethod
    def show_operation_menu() -> None:
        menu = {'1.Изменить', '2.Удалить', '3.Главное меню'}
        for i in menu:
            print(i)

    @staticmethod
    def get_balance(expence, income: []) -> float:
        balance = 0.0
        for i in expence:
            balance -= float(i[2])
        for i in income:
            balance += float(i[2])
        return balance


class Use_Case:

    def __init__(self) -> None:
        self.storage = Storage()
        self.view = View()

    def path_initialization(self):
        self.storage.path = 'path'
        with open(self.storage.path, 'a'):
            pass

    def add_expence(self, reason, price) -> None:
        self.storage.set(reason=reason, price=price, mode=E)
        self.storage.set_to_file()

    def add_income(self, reason, price) -> None:
        self.storage.set(reason=reason, price=price, mode=I)
        self.storage.set_to_file()

    def show_expence(self) -> None:
        print('\n\tРосходы: ')
        self.view.print_notes(self.storage.expence)

    def show_income(self) -> None:
        print('\n\tДоходы: ')
        self.view.print_notes(self.storage.income)

    def show_balance(self) -> float:
        return self.view.get_balance(expence=self.storage.expence, income=self.storage.income)

    def update(self, type: int, choose: int, reason, price: str) -> None:
        self.storage.update(type=type, choose=choose, reason=reason, price=price)
        self.storage.set_to_file()

    def remove(self, choose: int, type: int) -> None:
        self.storage.remove(choose=choose, type=type)
        self.storage.set_to_file()


def main() -> None:
    use_case = Use_Case()
    use_case.path_initialization()
    use_case.storage.get()
    while True:
        try:
            use_case.view.show_main_menu()
            choose = int(input('\n\tВыберите нужный вам раздел сверху: '))
            print()

            if choose == 1:
                reason, price = input('Введите причину росхода: '), float(input("Введите сумму росхода: "))
                use_case.add_expence(reason=reason, price=price)
                input("Нажмите ENTER для продолжения...")

            elif choose == 2:
                reason, price = input('Введите причину дохода: '), float(input("Введите сумму дохода: "))
                use_case.add_income(reason=reason, price=price)
                input("Нажмите ENTER для продолжения...")

            elif choose == 3:
                use_case.show_expence()
                input("Нажмите ENTER для продолжения...")

            elif choose == 4:
                use_case.show_income()
                input("Нажмите ENTER для продолжения...")

            elif choose == 5:
                print('\nВаш баланс: ', use_case.show_balance())
                input("Нажмите ENTER для продолжения...")

            elif choose == 6:
                chooseOps = int(input(f'\nВыберите нужную вам операцию снизу:\n\t'
                                      f'1.Изменение\n\t2.Удаление\n\t\tВыберите операцию: '))

                if chooseOps == 1:

                    type = int(input('\nИзменения над\n\t1.Росходами\n\t2.Доходами\n\t0.Главное меню\n\tВаш выбор: '))
                    if type == 1:
                        use_case.view.print_notes(use_case.storage.expence)
                    elif type == 2:
                        use_case.view.print_notes(use_case.storage.income)
                    elif type == 0:
                        return
                    else:
                        raise IndexError
                    change_choose = int(input('\nВыберите строку свыше для её изменения: '))
                    reason, price = input('\nИзменённая причина: '), float(input('Изменённая сумма: '))
                    use_case.update(type=type, choose=change_choose, reason=reason, price=price)
                    input("Нажмите ENTER для продолжения...")

                elif chooseOps == 2:
                    type = int(input('\nУдаление:\n\t1.Росхода\n\t2.Дохода\n\tВаш выбор: '))
                    if type == 1:
                        use_case.view.print_notes(use_case.storage.expence)
                    elif type == 2:
                        use_case.view.print_notes(use_case.storage.income)
                    elif type == 3:
                        return
                    else:
                        raise IndexError
                    remove_choose = int(input("Выберите строку свыше, для её удаления: "))
                    use_case.remove(choose=remove_choose, type=type)
                    input('Нажмите ENTER для продолжения...')

                elif chooseOps == 0:
                    return

                else:
                    print('Выбран неправильныый раздел операций!')
                    input('Нажмите ENTER, чтобы продолжить...')
            elif choose == 0:
                break
        except ValueError:
            print('\nВведены символы из другого мира!\nВведите числа от 0 до 6! ')
            input('\nВведено некорректное число\nНажмите ENTER для продолжения...')
        except IndexError:
            print('\nНеправильный выбор! Попробуйте заново!')
            input('\nВведено некорректное число\nНажмите ENTER для продолжения...')


if __name__ == '__main__':
    main()
