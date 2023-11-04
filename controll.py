import model as Model
from view import View

Expence = Model.Expence
Income = Model.Income


class Controller:

    def __init__(self) -> None:
        self.storage = Model.Storage()
        self.view = View
        with open(self.storage.path, 'a'):
            pass

    def path_initialization(self):
        self.storage.path = 'path'
        with open(self.storage.path, 'a'):
            pass

    def add_expence(self, reason, price) -> None:
        self.storage.set(reason=reason, price=price, mode=Expence)

    def add_income(self, reason, price) -> None:
        self.storage.set(reason=reason, price=price, mode=Income)

    def show_expence(self) -> None:
        print('\n\tРосходы: ')
        self.view.print_notes(self.storage.expence)

    def show_income(self) -> None:
        print('\n\tДоходы: ')
        self.view.print_notes(self.storage.income)

    def show_balance(self) -> float:
        return self.view.get_balance(expence=self.storage.expence, income=self.storage.income)

    def update(self, mode: int, choose: int, reason, price: str) -> None:
        self.storage.update(mode=mode, choose=choose, reason=reason, price=price)

    def remove(self, choose: int, mode: int) -> None:
        self.storage.remove(choose=choose, mode=mode)