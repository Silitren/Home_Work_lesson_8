class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма равна')
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


z_1 = Complex(5, 5)
z_2 = Complex(9, 6)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)

