"""
This is an example of an instance variable
"""

class MyClass():
  def __init__(self) -> None:
    self.count = 0
  def increment(self):
    self.count += 1