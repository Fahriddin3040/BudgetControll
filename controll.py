import model

EXPENCE = model.EXPENCE
INCOME = model.INCOME


class NoteController:

    note_model = model.NoteModel()

    def set_expence(self, reason: float, price: float) -> None:
        self.note_model.set(reason=reason, price=price, mode=EXPENCE)

    def set_income(self, reason: float, price: float) -> None:
        self.note_model.set(reason=reason, price=price, mode=INCOME)

    def get_balance(self) -> float:
        self.note_model.get_balance()
        return self.note_model.balance

    def update(self, mode: int, choose: int, reason: float, price: str) -> None:
        self.note_model.update(mode=mode, choose=choose, reason=reason, price=price)

    def remove(self, choose: int, mode: int) -> None:
        self.note_model.remove(choose=choose, mode=mode)

