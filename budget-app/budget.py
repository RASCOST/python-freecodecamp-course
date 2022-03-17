class Category:
    def __init__(ledger):
        self.ledger = ledger


    def deposit(self, amount, comment=''):
        ledger.append({'amount': amount, 'comment': comment})

    
