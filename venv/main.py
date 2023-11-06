from controll import Controller
import view



def press_enter():
    s = input("Нажмите ENTER для продолжения... если осмелитесь")


if __name__ == "__main__":
    controller = Controller()
    view = view.View()
    while True:
        view.show_main_menu()
        try:
            choose = int(input('\n\tВыберите нужный вам раздел сверху: '))
            print()

            if choose == 1:
                reason = input('\nВведите причину дохода: ')
                price = float(input("Введите сумму дохода: "))
                controller.set_expence(reason=reason, price=price)

            elif choose == 2:
                reason = input('\nВведите причину дохода: ')
                price = float(input("Введите сумму дохода: "))
                controller.set_income(reason=reason, price=price)
                press_enter()

            elif choose == 3:
                view.show_expence()
                press_enter()

            elif choose == 4:
                view.show_income()
                press_enter()

            elif choose == 5:
                view.show_balance()
                press_enter()

            elif choose == 6:
                chooseOps = int(input(f'\nВыберите нужную вам операцию снизу:\n\t'
                                      f'1.Изменение\n\t2.Удаление\n\t\tВыберите операцию: '))

                if chooseOps == 1:

                    mode = int(input('\nИзменения над\n\t1.Росходами\n\t2.Доходами\n\tВаш выбор: '))
                    if mode == 1:
                        view.show_expence()
                    elif mode == 2:
                        view.show_income()
                    elif mode == 3:
                        raise EOFError
                    else:
                        raise IndexError

                    change_choose = int(input('\nВыберите строку свыше для её изменения: '))
                    reason = input('\nВведите причину дохода: ')
                    price = float(input("Введите сумму дохода: "))
                    controller.update(mode=mode, choose=change_choose, reason=reason, price=price)
                    press_enter()

                elif chooseOps == 2:
                    mode = int(input('\nУдаление:\n\t1.Росхода\n\t2.Дохода\n\tВаш выбор: '))
                    if mode == 1:
                        view.show_expence()
                    elif mode == 2:
                        view.show_income()
                    elif mode == 3:
                        raise EOFError
                    else:
                        raise IndexError
                    remove_choose = int(input("Выберите строку свыше, для её удаления: "))
                    controller.remove(choose=remove_choose, mode=mode)
                    press_enter()

                elif chooseOps == 0:
                    break

                else:
                    print('Выбран неправильныый раздел операций!')
                    press_enter()
            elif choose == 0:
                break
        except ValueError:
            print('\nВведены символы из другого мира!\nВведите числа от 0 до 6! ')
            press_enter()
        except IndexError:
            print('\nНеправильный выбор! Попробуйте заново!')
            press_enter()
        except EOFError:
            pass


