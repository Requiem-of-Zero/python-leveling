class Employee:

  raise_amt = 1.05

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay

  @property # Allows .email to be invoked without ()
  def email(self):
    return f'{self.first}.{self.last}@email.com'
  
  @property # Allows .fullname to be invoked without ()
  def fullname(self):
    return f'{self.first} {self.last}'
  
  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)