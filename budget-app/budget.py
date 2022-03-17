class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []


    def deposit(self, amount, comment=''):
        self.ledger.append({'amount': amount, 'comment': comment})

    def withdraw(self,  amount, comment=''):
        if self.check_funds(amount):
            self.deposit(-amount, comment)
            return true
        return false

    def get_balance(self):
        total = 0

        for index=0 in len(self.ledger):
            total += self.ledger[index]['amount']

        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amout, f"Transfer to {category.name}")
            self.deposit(amout, f"Transfer from {self.name}")
            return true

        return false

    def check_funds(self, amount):
        if amount > self.get_balance():
            return false

        return true

    def __str__(self):
        cat_length = len(self.name)

        if 30 - cat_length % 2 == 0:
            title = '*' * (30 - cat_length) / 2
            title += self.name
            title += '*' * (30 - cat_length) / 2
        else:
            title = '*' * (30 - cat_length) / 2
            title += self.name
            title += '*' * (30 - ((30 - cat_length) / 2) - cat_length)
