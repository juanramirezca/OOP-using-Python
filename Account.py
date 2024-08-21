class Account():
  def __init__(self, name, balance, password):
    self.name = name
    self.balance = int(balance)
    self.password = password

  def deposit(self, amount, password):
    if password != self.password:
      print('Sorry, incorrect password')
      return None
    
    if amount < 0: 
      print('You cannot deposit a negative amount')
      return None
    
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount, password):
    if password != self.password:
      print('Sorry, incorrect password')
      return None
    
    if amount < 0: 
      print('You cannot withdraw a negative amount')
      return None
    
    self.balance -= amount
    return self.balance
  
  def get_balance(self, password):
    if password != self.password:
      print('Sorry, incorrect password')
      return None
    return self.balance
  
  def show(self):
    print(f'Name: {self.name}\nBalance: {self.balance}\nPassword: {self.password}\n')
