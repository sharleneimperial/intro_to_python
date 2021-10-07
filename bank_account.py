class BankAccount():
  def __init__(self):
    self.balance = 0
    self.interest_rate = .02

  def deposit(self, amount):
    if amount > 0:
      self.balance = self.balance + amount
      return(self.balance)
    else:
      return False

  def withdraw(self, amount):
    if self.balance - amount > 0:
      self.balance = self.balance - amount
      return(amount)
    else:
      return False

  def accumulate_interest(self):
        self.balance = self.balance*(1 + self.interest_rate)
        return(self.balance)

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.type = 'childs_account'
    self.interest_rate = 0

  def accumulate_interest(self):
    self.balance = self.balance + 10

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

class OverdraftAccount(BankAccount):
  def __init__(self, balance = 0):
    self.balance = balance
    self.overdraft_policy = 40
    self.interest_rate = 0
  
  def withdraw(self, withdraw_amount):
    if (self.balance - withdraw_amount) < 0:
      self.balance = self.balance - self.overdraft_policy
      return self.balance
    
  def accumulate_interest(self):
    return self.balance

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))

