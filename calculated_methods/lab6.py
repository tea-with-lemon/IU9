import sys
import numpy as np
from sympy import diff, symbols, sin

ideal = (1 + (5 ** 0.5)) / 2


def bisection(f, a, b, eps, i=0):
    c = (a + b) / 2
    dist = np.abs(a - b)
    i += 1
    if dist < 2 * eps:
        return c, i
    elif f(c) < f(c + eps):
        return bisection(f, a, c, eps, i)
    else:
        return bisection(f, c, b, eps, i)


def helper(b, a):
    global ideal
    return (a - b) / ideal


def golden(f, x0, x1, eps, i=0):
    alpha = x1 - helper(x0, x1)
    betha = x0 + helper(x0, x1)
    i += 1
    if np.abs(x1 - x0) < eps:
        return (x0 + x1) / 2, i
    elif f(alpha) >= f(betha):
        return golden(f, alpha, x1, eps, i)
    else:
        return golden(f, x0, betha, eps, i)


def newton(eps=10 ** (-5)):
    x, y = symbols('x y')
    func = x ** 2 + 10 * (y - sin(x)) ** 2
    f_x = diff(func, x)
    f_y = diff(func, y)
    f_xx = diff(func, x, x)
    f_xy = diff(func, x, y)
    f_yx = diff(func, y, x)
    f_yy = diff(func, y, y)
    val = np.array([1, 1])

    def grad(a, b):
        s = {x: a, y: b}
        return np.array([f_x.evalf(subs=s), f_y.evalf(subs=s)],
                        dtype=np.float64)

    def gesse(a, b):
        s = {x: a, y: b}
        return np.array([[f_xx.evalf(subs=s), f_xy.evalf(subs=s)],
                         [f_yx.evalf(subs=s), f_yy.evalf(subs=s)]],
                        dtype=np.float64)

    def next_iter(el):
        i = 0
        while True:
            i += 1
            p = np.linalg.solve(gesse(el[0], el[1]), grad(el[0], el[1]))
            next_el = el - p
            norm = np.amax(np.abs(p))
            if norm < eps:
                return next_el.tolist(), i
            else:
                el = next_el

    return next_iter(val)


np.set_printoptions(precision=14)
sys.setrecursionlimit(11000)
# print(golden(sin, 0, 1, 0.01))
# print(bisection(sin, 0, 1, 0.01))
print(newton())
