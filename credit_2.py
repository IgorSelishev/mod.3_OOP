class Wallet:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance
    
class GeneralWallet(Wallet):
    def get_balance(self):
        return f"Balance: {self.balance}"
    
wallet = Wallet()
print(wallet.get_balance())
wallet2 = GeneralWallet()
print(wallet2.get_balance())