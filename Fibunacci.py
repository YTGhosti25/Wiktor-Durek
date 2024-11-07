class FibonacciGenerator:
    def __init__ (self):
        self.a = 0
        self.b = 1
        self.lista = []
    def __call__ (self):
        self.lista.append(self.b)
        self.a, self.b = self.b,self.a + self.b

a = FibonacciGenerator()

for i in range(10):
    a()
print(a.lista)
