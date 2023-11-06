from controll import Controller


class View:

    def __init__(self):
        self.controller = Controller()

    def show_balance(self) -> None:
        balance = self.controller.get_balance()
        print(f"\n\tВаш баланс состовляет: {balance}")

    def show_expence(self) -> None:
        print('\n\tРосходы:')
        for i in range(0, len(self.controller.model.expence)):
            print(f'\t\t{i + 1}.Причина: {self.controller.model.expence[i][1]} .'
                  f' Сумма: {self.controller.model.expence[i][2]} . Дата: {self.controller.model.expence[i][3]}.')

    def show_income(self) -> None:
        print('\n\tДоходы:')
        for i in range(0, len(self.controller.model.income)):
            print(f'\t\t{i + 1}.Причина: {self.controller.model.income[i][1]} .'
                  f' Сумма: {self.controller.model.income[i][2]} . Дата: {self.controller.model.income[i][3]}.')

    @staticmethod
    def show_main_menu() -> None:
        menu = [
            "1.Добваить росход",
            "2.Добавить доход",
            "3.История росходов",
            "4.История доходов",
            "5.Баланс",
            "6.Операции",
            "0.Выход"
        ]
        for i in menu:
            print(i)

    @staticmethod
    def show_operation_menu() -> None:
        menu = {'1.Изменить', '2.Удалить', '3.Главное меню'}
        for i in menu:
            print(i)
