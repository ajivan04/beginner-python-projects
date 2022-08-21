class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    print "This account belongs to %s and contains $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print "User Balance: $%.2f" % (self.balance)
  def deposit(self, amount):
    if amount <= 0:
      print "Error, cannot deposit this amount. Please try again."
      return
    else:
      print "Depositing: $%.2f" % (amount)
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
      if amount > self.balance:
        print "Error, you cannot withdraw more than your current balance."
        return
      else:
        print "Withdrawing: $%.2f" % (amount)
        self.balance -= amount
        self.show_balance()

my_account = BankAccount("Abbas J")
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
my_account.show_balance()

