class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []


    def deposit(self, amount, comment=''):
        ledger.append({'amount': amount, 'comment': comment})

    def withdraw(self,  amount, comment=''):
        if get_balance() > amount:
            deposit(-amount, comment)
            return true
        return false

    def get_balance(self):
        total = 0

        for index=0 in len(self.ledger):
            total += self.ledger[index]['amount']

        return total

    def transfer(self, amount, category):
        if get_balance() > amount:
            withdraw(amout, f"Transfert to {category.name}")
            deposit(amout, f"Transfert from {self.name}")
            return true

        return false

