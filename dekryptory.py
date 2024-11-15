class AgeDescriptor():
  def __get__(self, instance, owner)
    return instance._age
  def __set__ (self, istance, value):
    if not isinstance(value,int):
      raise ValueError("wiek musi byc intem")
    if value < 18 or value > 100:
      raise ValueError("wiek musi być wiekszy niż 18, mniejszy niż 100")
    instance._age = value

class SalaryDescriptor():
  def __get__ (self, instance, ovner):
    return instance._salary
  def __set__(self,instance,value):
    if not isinstance(value, (int,float)):
      raise ValueError("wypłata musi byc liczbą")
    if value < 2000:
      raise ValueError("wynagrodzenie zbyt niskie")
    instance._salary = value

class Employee():
  age = AgeDescriptor()
  salary = SalaryDescriptor()

  def __init__ (self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary


