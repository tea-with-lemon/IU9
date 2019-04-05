from matplotlib.pyplot import *
from numpy import *
from functools import lru_cache

eps = 0.00000000001


def f(x):
    return 100 * (x ** 2 - 2) ** 3 + (x - 1) ** 2 - math.fabs(10 + x)


def svenn(x0):
    h = 0.0001
    k = 0
    left = x0 - h
    right = x0 + h
    x1, delta = None, None
    if f(left) >= f(x0) and f(x0) <= f(right):
        return [left, right]
    elif f(left) <= f(x0) and f(x0) >= f(right):
        print("Задайте другую начальную точку")
        return
    elif f(left) >= f(x0) >= f(right):
        delta = h
        left = x0
        x1 = x0 + h
        k = 1
    elif f(left) <= f(x0) <= f(right):
        delta = -h
        right = x0
        x1 = x0 - h
        k = 1
    while True:
        x_next = x1 + 2 ** k * delta
        if f(x_next) < f(x1) and delta == h:
            left = x1
            k += 1
        elif f(x_next) < f(x1) and delta == -h:
            right = x1
            k += 1
        elif f(x_next) >= f(x1):
            break
        x1 = x_next

    if delta == h:
        right = x_next
    elif delta == -h:
        left = x_next

    return [left, right]


def half_division(left, right, iter=0):
    if math.fabs(right - left) < eps:
        return (left + right) / 2, iter
    x = (left + right) / 2
    f1 = f(x - eps)
    f2 = f(x + eps)
    if f1 < f2:
        return half_division(left, x, iter+1)
    else:
        return half_division(x, right, iter+1)


def gold_section(f, left, right, iter=0):
    phi = (1 + math.sqrt(5)) / 2
    dest = right - left
    if dest < eps:
        return (right + left) / 2, iter
    x1 = right - dest / phi
    x2 = left + dest / phi
    y1 = f(x1)
    y2 = f(x2)

    if y1 >= y2:
        return gold_section(f, x1, right, iter+1)
    else:
        return gold_section(f, left, x2, iter+1)


@lru_cache()
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_method(left, right):
    n = 0
    dest = right - left
    while fib(n) <= dest / eps:
        n += 1

    k = 0
    x1 = left + dest * fib(n - 2) / fib(n)
    x2 = left + dest * fib(n - 1) / fib(n)

    while True:
        if f(x1) <= f(x2):
            right = x2
            x2 = x1
            x1 = left + (right - left)*fib(n - k - 3) / fib(n - k - 1)
        else:
            left = x1
            x1 = x2
            x2 = left + (right - left)*fib(n - k - 2)/fib(n - k - 1)
        if k == n - 3:
            x1_n = x1
            x2_n = x1_n + eps
            if f(x1_n) <= f(x2_n):
                left_n = left
                right_n = x2_n
            else:
                right_n = right
                left_n = x1_n
            return (left_n + right_n) / 2, k
        else:
            k+=1




def plot_f():
    x = linspace(-10, 10, 100)
    y = list(map(f, x))
    figure()
    plot(x, y, 'm')
    plot(gold_section(a, b)[0], 'b', marker='o')
    xlabel('x')
    ylabel('y')
    show()


a, b = svenn(-2)
print(gold_section(f, a, b))
'''
print(half_division(a, b))
print(a, b)

print(fib_method(a, b))
plot_f()
'''