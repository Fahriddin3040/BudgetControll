from controll import NoteController

EXPENCE = 1
INCOME = 2


class NoteView:

    def __init__(self):
        self.note_controller = NoteController()

    def show_balance(self) -> None:
        balance = self.note_controller.get_balance()
        print(f"\n\tВаш баланс состовляет: {balance}")

    def show_expence(self) -> None:
        print('\n\tРосходы:')
        for i in range(0, len(self.note_controller.note_model.expence)):
            print(f'\t\t{i + 1}.Причина: {self.note_controller.note_model.expence[i][1]} .'
                  f' Сумма: {self.note_controller.note_model.expence[i][2]} . Дата: {self.note_controller.note_model.expence[i][3]}.')

    def show_income(self) -> None:
        print('\n\tДоходы:')
        for i in range(0, len(self.note_controller.note_model.income)):
            print(f'\t\t{i + 1}.Причина: {self.note_controller.note_model.income[i][1]} .'
                  f' Сумма: {self.note_controller.note_model.income[i][2]} . Дата: {self.note_controller.note_model.income[i][3]}.')

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

    def set(self, mode: int, reason: str, price: float) -> None:
        if mode == 1:
            self.note_controller.set_income(reason=reason, price=price)
        elif mode == 2:
            self.note_controller.set_expence(reason=reason, price=price)

    def update(self, mode: int, choose: int, reason: int, price: int, ):
        self.note_controller.update(mode=mode, choose=choose, price=price, reason=reason)

    def remove(self, choose, mode):
        self.note_controller.remove(choose=choose, mode=mode)
