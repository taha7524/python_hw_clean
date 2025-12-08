import math


def square(d):
    return math.ceil(d*d)


num_d = float(input("Введите длину стороны: "))
print(f"Площадь квадрата: {square(num_d)}")
