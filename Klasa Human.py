class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"Nazywam się {self.name} i mam {self.age} lat"

class Builder(Human):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level
    def get_info(self):
        return f"Nazywam się {self.name} i mam {self.age} lat. Jestem budowiczym poziomu {self.level}"
class Sailor(Human):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level
    def get_info(self):
        return f"Nazywam się {self.name} i mam {self.age} lat. Jestem żeglarzem poziomu {self.level}"
class Pilot(Human):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level
    def get_info(self):
        return f"Nazywam się {self.name} i mam {self.age} lat. Jestem pilotem poziomu {self.level}"

# Bartek=Human('Bartek',20)
# print(Bartek.get_info())

# Maciek=Builder('Maciek', 22, 10)
# print(Maciek.get_info())

# Antek=Sailor('Antek', 28, 4)
# print(Antek.get_info())

# Franek=Pilot('Franek',30,7)
# print(Franek.get_info())

class Book:
    def __init__(self):
        self.author="autor"
        self.
    def nowa_ksiazka(self, author):
        self.author=author
    def __str__(self):
        return f"Autor: {self.author}"


# Driver Code
Rodger = Dog("rasa","kolor")
Rodger.setColor("brown")
print(Rodger.getColor())

ksiazka = Book()
ksiazka.nowa_ksiazka("ktos")
print(ksiazka)
