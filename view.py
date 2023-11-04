Expence = 1
Income = 2



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
        menu = menu = {
    1: "1.Добваить росход",
    2: "2.Добавить доход",
    3: "3.История росходов",
    4: "4.История доходов",
    5: "5.Баланс",
    6: "6.Операции",
    7: "0.Выход"
        }
        for i in range(1, len(menu) + 1):
            print(menu[i])

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
