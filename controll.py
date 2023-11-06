import model

Expence = model.Expence
Income = model.Income


class Controller:

    model = model.Model()

    def set_expence(self, reason=float, price=float) -> None:
        self.model.set(reason=reason, price=price, mode=Expence)

    def set_income(self, reason=float, price=float) -> None:
        self.model.set(reason=reason, price=price, mode=Income)

    def get_balance(self) -> float:
        self.model.get_balance()
        return self.model.balance

    def update(self, mode=int, choose=int, reason=float, price=str) -> None:
        self.model.update(mode=mode, choose=choose, reason=reason, price=price)

    def remove(self, choose=int, mode=int) -> None:
        self.model.remove(choose=choose, mode=mode)

