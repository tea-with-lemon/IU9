from numpy.linalg import inv

from lab4 import f, grad
from scipy import optimize
import numpy as np


def g_array():
    return [lambda x: x[0] ** 2 + x[1] ** 2 - 10, lambda x: -x[0], lambda x: -x[1]]


def g_der():
    return lambda x: np.array([
        [2 * x[0], 2 * x[1]],
        [-1, 0],
        [0, -1]
    ])


def p(x, r):
    return r / 2 * (max(0, (x[0] ** 2 + x[1] ** 2 - 10)) ** 2 + max(0, (-x[0])) ** 2 + max(0, -x[1]) ** 2)


def penalty_out_methods(f, x0, r0, c=10, e=10 ** -8, max_iter=10):
    r = r0
    k = 0
    while k < max_iter:
        k += 1
        help_f = lambda x: f(x) + p(x, r)
        search_res = optimize.minimize(help_f, x0, method='CG')
        x0 = search_res.x
        res_p = p(x0, r)
        if res_p <= e:
            break
        r *= c
    return [k, x0, f(x0)]


print("Метод штрафных функций: " + str(penalty_out_methods(f, [2, 2], 1)))


def p_in(x, r):
    return -r * (1 / (x[0] ** 2 + x[1] ** 2 - 10) - 1 / x[0] - 1 / x[1])


def penalty_in_method(f, x0, r0, c=10, e=10 ** -8, max_iter=100):
    r = r0
    x = x0
    k = 0
    while k < max_iter:
        k += 1
        help_f = lambda x: f(x) + p_in(x, r)
        search_res = optimize.minimize(help_f, x, method='CG')
        x = search_res.x
        res_p = p_in(x, r)
        if res_p < e:
            break
        r /= c
    return [k, x, f(x)]


print("Метод внутренних штрафов" + str(penalty_in_method(f, [3, 2], 1)))


def lagrange(f, x0, r0=1, c=3, e=10 ** -8, max_iter=1000):
    g = g_array()
    r = r0
    u = np.random.random(len(g))
    x = x0
    k = 0
    while k < max_iter:
        k += 1
        l = lambda x: f(x) + 1 / (2 * r) * sum([max([0, u[i] + r * gf(x)]) ** 2 - u[i] ** 2 for i, gf in enumerate(g)])

        search_res = optimize.minimize(l, x, method='CG')
        next_x = search_res.x
        x = next_x
        p = 0.5 * sum([max([0, u[i] + r * gf(x)]) ** 2 - u[i] ** 2 for i, gf
                       in enumerate(g)]) / r
        if p <= e:
            return [k, x, f(x)]
        r *= c
        u = [max(0, u[i] + r * gf(x)) for i, gf in enumerate(g)]

    return [k, x, f(x)]


def gradient(f, x0, e=10 ** -8, max_iter=100):
    x = x0
    k = 0
    case = 0
    deltax = 0.0001
    g = g_array()
    dg = g_der()
    gradf = grad(x)
    id = np.eye(3)
    np.delete(id, 2)

    while k < max_iter:
        for gf in g:
            if -e <= gf(x) and gf(x) <= 0:
                case = 1
                break
        if case:
            gf = gradf
            A = dg(x)
            if gf == 0:
                la = np.matmul(np.matmul(inv(np.matmul(dg(x), A.transpose())), A),
                               np.array([gradf(x).tolist()]).transpose()).transpose().reshape(-1)
                if la <= 0:
                    return [k, x, f(x)]
                max_la = 0
                max_i = 0
                for i, elem in enumerate(la):
                    if elem < 0:
                        max_la = min([max_la, elem])
                        max_i = i
                np.delete(A, max_i)
            else:
                deltax = - inv(id - np.matmul(A.transpose(), np.matmul(A, A.transpose())))
                if deltax < e:
                    la = np.matmul(np.matmul(inv(np.matmul(dg(x), A.transpose())), A),
                                   np.array([gradf(x).tolist()]).transpose()).transpose().reshape(-1)

                    if la <= 0:
                        return [k, x, f(x)]
                    max_la = 0
                    max_i = 0
                    for i, elem in enumerate(la):
                        if elem < 0:
                            max_la = min([max_la, elem])
                            max_i = i
                    np.delete(A, max_i)
            helper = lambda alpha: x + alpha * deltax
            alpha = optimize.minimize(helper, x, 'CG')
            x = x + alpha * deltax
    return [k, x, f(x)]


print("Метод Лагранжа: " + str(lagrange(f, [2, 2])))
print(str(gradient(f, [2, 2])))