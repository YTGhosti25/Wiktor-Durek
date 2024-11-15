class MyMeta(type):
    def __new__(cls, name, bases, dct):
        #Dodanie atrybutu klasy
        dct['class_id'] = 12345
        # Zmodywikwanie metody klasy
        original_method = dct.get('say_hello')
        if original_method:
            def new_method(self):
                print(f"hello from {self.__class__.__name__}")
            dct['say_hello'] = new_method
        #tworzenie klasy
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    def say_hello(self):
        print("helo")
        print("afafa")


obj = MyClass()

obj.say_hello()
print(obj.class_id)


class Base1:
    def method_from_base1(self):
        print("method from base1")
class Base2:
    def method_from_base2(self):
        print("method from base2")

class MyMeta2(type)
