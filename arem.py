from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')


def calculatesquareroot(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    if your_number <= 0:
        return print('root = 0')
    return print(f'Мы вычислили квадратный корень из введённого вами числа. '
                 f'Это будет: {calculatesquareroot(your_number)}')


print(message)
calc(25.5)
