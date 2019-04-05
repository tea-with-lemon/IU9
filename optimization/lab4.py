import copy

from sympy import Symbol
from numpy import eye, array, matmul, copy, linalg, random, dot
from scipy.optimize import minimize_scalar
from lab3_1 import gold_section, svenn

n = 2


def f(x, n=2, a=15, b=2, f0=40):
    return sum([a * (x[i] ** 2 - x[i + 1]) ** 2 + b * (x[i] - 1) ** 2 for i in range(0, n - 1)]) + f0


def grad(x, a=158, b=2):
    return array([4 * a * x[0] * (x[0] ** 2 - x[1]) + 2 * b * (x[0] - 1),
                  -2 * a * (x[0] ** 2 - x[1])])


def fletcher_reeves(x, step=0, d_prev=0, x_prev=0, delta=0.001, eps=0.001):
    d = -grad(x)
    if step > 0:
        d += d_prev * (linalg.norm(grad(x)) / linalg.norm(grad(x_prev))) ** 2
    alpha = gold_section(lambda alpha: f(x + d * alpha), svenn(1)[0], svenn(1)[1])[0]

    # alpha = minimize_scalar(lambda alpha: f(x + d * alpha), bounds=(-max_step, max_step), method='Golden')
    new_x = x + alpha * d
    if abs(linalg.norm(x - new_x)) < delta and f(x) - f(new_x) < eps:
        return f(new_x), new_x, step
    return fletcher_reeves(new_x, step + 1, d, x)

def polak_ribier(x, step=0, d_prev=0, x_prev=0, delta=0.001, eps=0.001):
    d = -grad(x)
    if step > 0:
        d += d_prev * dot(grad(x), grad(x) - grad(x_prev))/linalg.norm(grad(x_prev))**2
    alpha = gold_section(lambda alpha: f(x + d * alpha), svenn(1)[0], svenn(1)[1])[0]
    new_x = x + alpha * d
    if abs(linalg.norm(x - new_x)) < delta and f(x) - f(new_x) < eps:
        return f(new_x), new_x, step
    return fletcher_reeves(new_x, step + 1, d, x)


def get_step_point(x, h, i):
    x = copy(x)
    x[i] += h
    return x


def exploring_search(f, x0, e=1e-5):
    global xp

    def f_opt(h):
        return f(get_step_point(x, h, i))

    x = x0
    while True:
        for i in range(len(x)):
            xp = x
            x = get_step_point(x, minimize_scalar(f_opt).x, i)
        if sum(x - xp) * 1.0 / len(x) < e:
            break
    return x


def pattern_search(f, x0, e=1e-3, l=2.0):
    step = 0
    while True:
        step += 1
        x1 = x0
        x2 = exploring_search(f, x0)
        x3 = x1 + l * (x2 - x1)
        x4 = exploring_search(f, x3)
        if linalg.norm((x2 - x4)) / len(x0) < e:
            break
        else:
            x0 = x2
    return f(x2), x2, step


def nelder_mead(f, x_start,
                step=0.1, no_improve_thr=10e-6,
                no_improv_break=10, max_iter=0,
                alpha=1., gamma=2., rho=-0.5, sigma=0.5):
    dim = len(x_start)
    prev_best = f(x_start)
    no_improv = 0
    res = [[x_start, prev_best]]

    for i in range(dim):
        x = copy(x_start)
        x[i] = x[i] + step
        score = f(x)
        res.append([x, score])

    iters = 0
    while True:
        res.sort(key=lambda x: x[1])
        best = res[0][1]

        if max_iter and iters >= max_iter:
            return res[0]
        iters += 1

        if best < prev_best - no_improve_thr:
            no_improv = 0
            prev_best = best
        else:
            no_improv += 1

        if no_improv >= no_improv_break:
            return res[0], iters

        x0 = [0.] * dim
        for tup in res[:-1]:
            for i, c in enumerate(tup[0]):
                x0[i] += c / (len(res) - 1)

        xr = x0 + alpha * (x0 - res[-1][0])
        rscore = f(xr)
        if res[0][1] <= rscore < res[-2][1]:
            del res[-1]
            res.append([xr, rscore])
            continue

        if rscore < res[0][1]:
            xe = x0 + gamma * (x0 - res[-1][0])
            escore = f(xe)
            if escore < rscore:
                del res[-1]
                res.append([xe, escore])
                continue
            else:
                del res[-1]
                res.append([xr, rscore])
                continue

        xc = x0 + rho * (x0 - res[-1][0])
        cscore = f(xc)
        if cscore < res[-1][1]:
            del res[-1]
            res.append([xc, cscore])
            continue

        x1 = res[0][0]
        nres = []
        for tup in res:
            redx = x1 + sigma * (tup[0] - x1)
            score = f(redx)
            nres.append([redx, score])
        res = nres


def DFP(x, step=0, x_prev=0, G=eye(n), eps1=0.001, eps2=0.001, delta=0.001, m=1000):
    d = -grad(x)
    if linalg.norm(d) < eps1 or step > m:
        return f(x), x, step
    if step > 0:
        delta_g = array([grad(x) - grad(x_prev)])
        delta_x = array([x - x_prev])
        G += matmul(delta_x.transpose(), delta_x) / matmul(delta_x, delta_g.transpose()) - \
             matmul(matmul(matmul(G, delta_g.transpose()), delta_g), G) / matmul(matmul(delta_g, G),
                                                                                 delta_g.transpose())

        d = matmul(-G, array([grad(x)]).transpose()).transpose()[0]

    alpha = minimize_scalar(lambda alpha: f(x + alpha * d), method='Golden')
    new_x = x + alpha.x * d

    if abs(linalg.norm(x - new_x)) < delta and abs(f(x) - f(new_x)) < eps2:
        return f(new_x), new_x, step
    return DFP(new_x, step + 1, x, G)


xx = Symbol('x')
yy = Symbol('y')

my_function = 158 * ((xx ** 2 - yy) ** 2) + 2 * ((xx - 1) ** 2) + 40
syms = [xx, yy]


def Hessian(x):
    return array([[1896 * x[0] ** 2 - 632 * x[1] + 4, -632 * x[0]],
                  [-632 * x[0], 316]])


def levenberg_markvardt(x, step=0, m=10000, eps=0.0001, M=1000):
    d = grad(x)
    if linalg.norm(d) < eps or step > M:
        return f(x), x, step
    while True:
        d = matmul(linalg.inv(-(Hessian(x) + m * eye(n))), d.transpose())
        new_x = x + d
        if f(new_x) < f(x):
            return levenberg_markvardt(new_x, step + 1, m / 2.)
        m *= 2


def gradient_descent(x, nm='Golden', eps=0.0005, steps=0):
    result = minimize_scalar(lambda alpha: f(x - alpha * grad(x)), method=nm)
    new_x = x - result.x * grad(x)
    if abs(f(x) - f(new_x)) < eps:
        return f(x), x, steps
    return gradient_descent(new_x, nm, steps=steps + 1)

print("Проекция градиента: "+str(gradient_descent(random.random(n))))
'''
start_point = random.random(n)
print("Стартовая точка: " + str(start_point) + ", значение в ней: " + str(f(start_point)))
print("Полак Рибьер: "+ str(polak_ribier(start_point)))
print("Флетчер-Ривс: " + str(fletcher_reeves(start_point)))
print("Метод конфигураций: " + str(pattern_search(f, start_point)))
print("Нелдер-Мид: " + str(nelder_mead(f, start_point)))
print("Метод Девидона-Флетчера-Пауэлла: " + str(DFP(start_point)))
print("Метод Левенберга Марквардта: " + str(levenberg_markvardt(start_point)))
print("Градиентный спуск: " + str(gradient_descent(start_point)))
'''