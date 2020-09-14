class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.current_balance = 0
    self.total_withdraw = 0

  def __str__(self):
    line = '{:*^30}\n'.format(self.name)
    for item in self.ledger:
      line += '{:<23}{:>7.2f}\n'.format(item['description'][:23], item['amount'])

    line += "Total: {:.2f}".format(self.current_balance)
    return line

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.current_balance += amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": - amount, "description": description})
      self.current_balance -= amount
      self.total_withdraw += amount
      return True
    else:
      return False

  def get_balance(self):
    return self.current_balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    return self.current_balance >= amount


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food)

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(clothing)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(auto)


def create_spend_chart(categories):

  pass

create_spend_chart([food, clothing, auto])