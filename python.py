class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

karlee = User("Karlee")
joshua = User("Joshua")
joseph = User("Joseph")


karlee.make_deposit(10)
karlee.make_deposit(30)
karlee.make_deposit(20)
karlee.make_withdrawl(5)
karlee.display_user_balance()

joshua.make_deposit(25)
joshua.make_deposit(100)
joshua.make_withdrawl(15)
joshua.make_withdrawl(20)
joshua.display_user_balance()

joseph.make_deposit(300)
joseph.make_withdrawl(50)
joseph.make_withdrawl(25)
joseph.make_withdrawl(100)
joseph.display_user_balance()
