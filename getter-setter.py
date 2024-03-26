class Bank:
    def __init__(self, init) -> None:
        self.__deposit = init

    @property
    def deposite(self):
        return self.__deposit

    @deposite.setter
    def deposite(self, value):
        if value < 0:
            return "error"
        self.__deposit += value


new_bank = Bank(200)
new_bank.deposite = 500
print(new_bank.deposite)
