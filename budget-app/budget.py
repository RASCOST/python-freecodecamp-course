class Category:
    def __init__(self, ledger):
        self.ledger = ledger


    def deposit(self, amount, comment=''):
        ledger.append({'amount': amount, 'comment': comment})

    def withdraw(self,  amount, comment=''):
        if get_balance() >= amount:
            deposit(-amount, comment)
            return true
        return false

    def get_balance(self):
        total = 0

        for index=0 in len(self.ledger):
            total += self.ledger[index]

        return total
