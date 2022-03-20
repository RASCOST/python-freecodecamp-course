class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []


    def deposit(self, amount, comment=''):
        self.ledger.append({'amount': amount, 'description': comment})

    def withdraw(self,  amount, comment=''):
        if self.check_funds(amount):
            self.deposit(-amount, comment)
            return True
        return False

    def get_balance(self):
        total = 0

        for index in range(len(self.ledger) - 1):
            total += self.ledger[index]['amount']

        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amout, f"Transfer to {category.name}")
            self.deposit(amout, f"Transfer from {self.name}")
            return True

        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False

        return True

    def title(self):
        cat_length = len(self.name)

        if 30 - cat_length % 2 == 0:
            title = '*' * int((30 - cat_length) / 2)
            title += self.name
            title += '*' * int((30 - cat_length) / 2)
        else:
            title = '*' * int((30 - cat_length) / 2)
            title += self.name
            title += '*' * (30 - int((30 - cat_length) / 2) - cat_length)

        title += '\n'

        return title

    def list_items(self):
        items = ''

        for item in self.ledger:
            # first 23 char
            if len(item['description']) > 24:
                description = item['description'][:22]
            else:
                description = item['description']

            # 2 decimal places and no more tha 7 char
            amount = "{:.2f}".format(item['amount'])

            if len(amount) > 8:
                amount = amount[:6]

            items += description + ' ' * (30 - len(description) - len(amount)) + amount + '\n'

        return items

    def total(self):
        total = 'Total:' + ' ' + str(self.get_balance()) + '\n'

    def __str__(self):
        return f"{self.title()}{self.list_items()}{self.total()}"
