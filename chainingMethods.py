class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.acct_balance = 0

    def make_deposit(self,amount):
        self.acct_balance += amount
        return self
    
    def display_user_balance(self):
        print(f"Name: {self.name}, Balance: {self.acct_balance}")

    def transfer_money(self, amount, other_user):
        self.acct_balance = self.acct_balance - amount
        other_user.acct_balance = other_user.acct_balance + amount 
        print(f"{self.name} just transferred {amount} dollars to {other_user.name}")
        return self


rachel = User("Rachel","rachelp5446@gmail.com")
kilo = User("Kilo","kilo@dogmail.com")
kenobi = User("Kenobi","kenobi@dogmail.com")

rachel.make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(-250).display_user_balance()
kilo.make_deposit(1000).make_deposit(1000).make_deposit(-500).make_deposit(-500).display_user_balance()
kenobi.make_deposit(800).make_deposit(-100).make_deposit(-100).make_deposit(-100).display_user_balance()

kilo.display_user_balance()
rachel.display_user_balance()
rachel.transfer_money(200,kilo)
kilo.display_user_balance()
rachel.display_user_balance()
