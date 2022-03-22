import re

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
        for index in range(len(self.ledger)):
            total += self.ledger[index]['amount']

        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
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
                description = item['description'][:23]
            else:
                description = item['description']

            # 2 decimal places and no more tha 7 char
            amount = "{:.2f}".format(item['amount'])

            if len(amount) > 8:
                amount = amount[:6]

            items += description + ' ' * (30 - len(description) - len(amount)) + amount + '\n'

        return items

    def total(self):
        return 'Total: ' + str(self.get_balance())

    def __str__(self):
        return f"{self.title()}{self.list_items()}{self.total()}"

def create_spend_chart(categories):
    chart = 'Percentage spent by category' + '\n'
    percentages = []

    # get the percentages
    for category in categories:
        total = 0
        if not category.ledger:
            percentages.append(0)
            break

        for idx in range(len(category.ledger)):
            if category.ledger[idx]['amount'] < 0:
                total += abs(category.ledger[idx]['amount'])

        percentages.append(round(100 * total / category.ledger[0]['amount']))

    # create the bargraph
    for y in range(100, -10, -10):
        chart += f"{' ' * (3 - len(str(y)))}{str(y)}|"
        for percentage in percentages:
            if percentage >= y:
                chart += ' o '
        chart += '\n'

    # x line
    chart += ' ' * 4 + '---' * len(categories) + '-\n'

    # write x legend
    idx = 0
    while True:
        chart += ' ' * 4
        line = ''
        for category in categories:
            if idx <= len(category.name) - 1:
                line += ' ' + category.name[idx] + ' '
            else:
                line += ' ' * 3

        if not re.search('[a-zA-Z]', line):
            break
        else:
            chart += line + '\n'
            idx += 1

    return chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food)
# print(clothing)

print(create_spend_chart([food, clothing, auto]))
