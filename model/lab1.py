import math
from scipy.integrate import odeint
import matplotlib.pylab as plt

v_0 = 50
alpha = math.pi / 4
g = 9.8
t = 0
x = 0

beta = 5
p = 11340


# Модель Галилея

def galiley(v_0, alpha, g):
    return math.tan(alpha) * (2 * v_0 ** 2 * math.cos(alpha) ** 2) / g


print(galiley(v_0, alpha, g))


# Модель Ньютона

def runge_step(t, start, functions, step_size):
    iter = len(functions)
    k1 = []
    k2 = []
    k3 = []
    k4 = []

    for i in range(iter):
        k1.append(functions[i](t, start) * step_size)

    for i in range(iter):
        tmp = []
        for j in range(len(k1)):
            tmp.append(k1[j] / 2 + start[j])
        k2.append(functions[i](t + step_size / 2, tmp) * step_size)

    for i in range(iter):
        tmp = []
        for j in range(len(k1)):
            tmp.append(k2[j] / 2 + start[j])
        k3.append(functions[i](t + step_size / 2, tmp) * step_size)

    for i in range(iter):
        tmp = []
        for j in range(len(k1)):
            tmp.append(k3[j] / 2 + start[j])
        k4.append(functions[i](t + step_size, tmp) * step_size)

    res = []
    for i in range(iter):
        res.append(start[i] + (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6)

    return res


def gen_func(params):
    m, g, beta = params

    def dx(t, args):
        x, y, u, w = args
        return u

    def dy(t, args):
        x, y, u, w = args
        return w

    def du(t, args):
        x, y, u, w = args
        return (- beta * u * math.sqrt(u ** 2 + w ** 2)) / m

    def dw(t, args):
        x, y, u, w = args
        return (- m * g - beta * w * math.sqrt(u ** 2 + w ** 2)) / m

    return [
        dx,
        dy,
        du,
        dw
    ]


def weight(r):
    volume = 4 / 3 * math.pi * r ** 3
    return volume * p


def vectorfield(initial, t, params):
    x, y, u, w = initial
    m, g, beta = params

    f = [u,
         w,
         (- beta * u * math.sqrt(u ** 2 + w ** 2)) / m,
         (- m * g - beta * w * math.sqrt(u ** 2 + w ** 2)) / m]

    return f


def scipy_newton(r, g=9.8):
    m = weight(r)
    initial = [0, 0, v_0 * math.cos(alpha), v_0 * math.sin(alpha)]
    stoptime = 1000.0
    numpoints = 25000
    t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]
    solution = odeint(vectorfield, initial, t, args=([m, g, beta],))
    return solution, t


def newton_runge(r, g=9.8):
    m = weight(r)
    step = 0.01
    initial = [0, 0, v_0 * math.cos(alpha), v_0 * math.sin(alpha)]
    start_time = 0
    f = gen_func([m, g, beta])
    t = [start_time]
    res = [initial]
    i = 0
    while res[i][1] >= 0:
        next = runge_step(t[i], res[-1], f, step)
        res.append(next)
        t.append(t[-1] + step)
        i += 1
    return res, t


def output():
    # res, time = scipy_newton(0.15)
    res, time = newton_runge(0.15)
    print(res)
    i = 0

    while res[i][1] >= 0:
        i += 1

    res = res[:i + 1]

    x_gal = []
    y_gal = []
    time_stop = galiley(v_0, alpha, g) / (v_0 * math.cos(alpha))

    gal_time = [time_stop * float(i) / (100 - 1) for i in range(100)]

    for t in gal_time:
        x_gal.append(v_0 * math.cos(alpha) * t)
        y_gal.append(v_0 * math.sin(alpha) * t - (g * t ** 2) / 2)

    print(y_gal)
    x_ar, y, u, v = [], [], [], []
    for i in range(len(res)):
        x_ar.append(res[i][0])
        y.append(res[i][1])
        u.append(res[i][2])
        v.append(res[i][-1])
    print(x_ar)

    plt.figure(figsize=(6, 4.5))

    plt.xlabel('t')
    plt.grid(True)
    lw = 1

    plt.plot(x_ar, y, 'b', linewidth=lw)
    plt.plot(x_gal, y_gal, 'g', linewidth=lw)

    plt.legend((r'$Newton$', r'$Galiley$'))

    plt.savefig('ballistic.png', dpi=100)


output()
