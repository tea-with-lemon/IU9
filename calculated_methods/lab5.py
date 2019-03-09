import math
import lab1


def solve_diff(start, end):
    n = 10
    y_start = math.exp(start)
    y_end = math.exp(end)
    abs_error = []
    x = []
    f = []
    y = []
    d = []
    a = []
    b = []
    c = []
    e = []
    p = q = 1
    h = (end - start) / n
    for i in range(0, n + 1):
        f.append(math.exp(start + h * i) * 3)
        e.append(math.exp(start + h * i))
        x.append(start + h * i)
    for i in range(0, n - 2):
        a.append(1 - (p * h) / 2)
        c.append(1 + (p * h) / 2)
    for i in range(0, n - 1):
        b.append(q * h ** 2 - 2)
    d.append(f[1] * h ** 2 - y_start * (1 - (p * h) / 2))
    for i in range(2, n - 1):
        d.append(f[i] * h ** 2)
    d.append(f[n - 1] * h ** 2 - y_end * (1 + (p * h) / 2))
    lab1.createHelper(a, b, c, d, n)
    y = [y_start] + lab1.createX(a, b, d, n) + [y_end]
    for i in range(0, len(f)):
        abs_error.append(math.fabs(e[i] - y[i]))
    for i in range(0, len(y)):
        print("значениe x: " + str(x[i]) + "| y точный " + str(e[i]) + "| найденный y : " + str(y[i])
              + "| абсолютная погрешность " + str(abs_error[i])+"|")


print(solve_diff(0, 1))
