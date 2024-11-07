#dekorator
import time
import functools
def imie(imie):
    def moj_dekorator(funkcja):
        def opakowanie(*args,**kwargs):
            start = int(time.time())
            print(f"przed wywołaniem {imie}")
            wynik = funkcja(*args,**kwargs)
            time.sleep(1)
            print("po wywołaniu")
            end = int(time.time())
            print("zajeło to",end-start)
            return wynik
        return opakowanie
    return moj_dekorator

class LicznikWywolan:
    def __init__(self,funkcja):
        self.funkcja = funkcja
        self.licznik = 0

    def __call__(self,*args,**kwargs):
        self.licznik += 1
        print("wywolano",self.licznik, "razy")
        return self.funkcja(*args,**kwargs)

@imie("bartek")
def przykładowa_funkcja(a,b):
    return a+b

def count_calls(function):
    def wrapper(*args,**kwargs):
        if not hasattr(wrapper,"call_count"):
            wrapper.call_count = 0
        wrapper.call_count += 1
        print(f"Funkcja {function.__name__} wywolana byla {wrapper.call_count}")
        return function(*args,**kwargs)
    return wrapper

class FunctionCallTraker:
    def __init__(self,funkcja):
        self.funkcja = count_calls(funkcja)
        self.total_calls = 0
    def reset (self):
        self.total_calls=0
        if not hasattr(self.funkcja,"call_count"):
            self.funkcja.call_count = 0
    def __call__(self,*args,**kwargs):
        self.total_calls += 1
        return self.funkcja(*args,**kwargs)


@FunctionCallTraker
def Mnoż(a,b):
    return a*b




print(Mnoż(2,5))
print(Mnoż(3,5))
print(f"total calls: (FunctionCallTraker): {Mnoż.total_calls}")

