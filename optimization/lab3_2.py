import math
import numpy

def f(x):
    return 100 * (x ** 2 - 2) ** 3 + (x - 1) ** 2 - math.fabs(10 + x)


def quadric(x0=-2):
    step = 0.0001
    eps = 0.00001
    delta = 0.0001
    x1 = x0 + step
    if f(x0) > f(x1):
        x2 = x0 + 2 * step
    else:
        x2 = x0 - 2* step

    while True:
        m = min(f(x0), f(x1), f(x2))
        x_min = eval('x' + str(numpy.argmin([f(x0), f(x1), f(x2)])))
        try:
            a = ((x1**2 - x2**2)*f(x0) + (x2**2 - x0**2)*f(x1) + (x0**2 - x1**2)*f(x2))/\
                (2* ((x1 - x2)*f(x0) + (x2- x0)*f(x1) + (x0 - x1)*f(x2)))
        except ZeroDivisionError:
            return quadric(x_min)
        if math.fabs((m - f(a))/f(a)) < eps and math.fabs((x_min - a)/a) < delta:
            return a
        else:
            if not(a >= x0 and a <= x2):
                return quadric(a)
            else:
                if a < x1:
                    x2 = x1
                    x1 = a
                else:
                    x0 = x1
                    x1 = a
                continue
print(quadric())
