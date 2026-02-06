class Bankaccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self,amount):
         if self.balance >= amount:
            self.balance -= amount
            self.display_balance()
         else:
             print("Not enough funds to deposit.")

    def display_balance(self):
        print("The account number is:", self.balance)

class SavingsAccount(Bankaccount):
    def __init__(self, intrest_rate, account_holder):
        temp_intrest=intrest_rate/100
        self.intrest_rate = temp_intrest
        super().__init__(account_holder)

    def add_intrest(self):
        # interest = self.balance * self.intrest_rate / 100
        self.balance*=(1+self.intrest_rate)
        super().display_balance()


class CurrentAccount(Bankaccount):
    def __init__(self, overdraft_limit,name):
        self.overdraft_limit = overdraft_limit
        super().__init__(name)
    def withdraw_with_overdraft(self, amount):
        if amount<self.balance+self.overdraft_limit:
              super().display_balance()
        else:
            print("withdraw exceeded.")

Save = SavingsAccount(20,"raju")
Current = CurrentAccount(100, "raja")

Save.deposit(100)
Save.withdraw(30)
Save.add_intrest()



