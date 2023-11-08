import view

EXPENCE = 1
INCOME = 2

def main():
    def press_enter(): s = input('Нажмите на ENTER для продолжения...')
    note_view = view.NoteView()

    while True:

        note_view.show_main_menu()
        try:
            choose = int(input('\n\tВыберите нужный вам раздел сверху: '))
            print()

            if choose == 1:
                reason = input('\nВведите причину дохода: ')
                price = float(input("Введите сумму дохода: "))
                note_view.set(mode=EXPENCE, reason=reason, price=price)
                press_enter()

            elif choose == 2:
                reason = input('\nВведите причину дохода: ')
                price = float(input("Введите сумму дохода: "))
                note_view.set(mode=INCOME, reason=reason, price=price)
                press_enter()

            elif choose == 3:
                note_view.show_expence()
                press_enter()

            elif choose == 4:
                note_view.show_income()
                press_enter()

            elif choose == 5:
                note_view.show_balance()
                press_enter()

            elif choose == 6:
                chooseOps = int(input(f'\nВыберите нужную вам операцию снизу:\n\t'
                                      f'1.Изменение\n\t2.Удаление\n\t\tВыберите операцию: '))

                if chooseOps == 1:

                    mode = int(input('\nИзменения над\n\t1.Росходами\n\t2.Доходами\n\t0.Главное меню\n\tВаш выбор: '))
                    if mode == EXPENCE:
                        note_view.show_expence()
                    elif mode == INCOME:
                        note_view.show_income()
                    elif mode == 0:
                        return
                    else:
                        raise IndexError

                    change_choose = int(input('\nВыберите строку свыше для её изменения: '))
                    reason = input('\nВведите причину дохода: ')
                    price = float(input("Введите сумму дохода: "))
                    note_view.update(mode=mode, choose=change_choose, price=price, reason=reason)

                elif chooseOps == 2:
                    mode = int(input('\nУдаление:\n\t1.Росхода\n\t2.Дохода\n\t0.Главное меню\n\tВаш выбор: '))
                    if mode == EXPENCE:
                        note_view.show_expence()
                    elif mode == INCOME:
                        note_view.show_income()
                    elif mode == 0:
                        return
                    else:
                        raise IndexError
                    remove_choose = int(input("Выберите строку свыше, для её удаления: "))
                    note_view.remove(choose=remove_choose, mode=mode)
                elif chooseOps == 0:
                    return

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



if __name__ == '__main__':
    main()