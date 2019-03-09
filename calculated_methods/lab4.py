import math

k = 2


def calculate_int_h(a, b, n):
    x = []
    y = []
    x_centr = []
    y_centr = []
    sum_centr_rect = 0
    sum_trap = 0
    ans = dict.fromkeys(['centr_rect', 'trap'])
    h = (b - a) / n
    for i in range(0, n + 1):
        y.append(math.exp(a + h * i))
        x.append(a + h * i)
    for i in range(0, n):
        x_centr.append((x[i] + x[i + 1]) / 2)
        y_centr.append(math.exp(x_centr[i]))
        sum_centr_rect += y_centr[i]
    sum_centr_rect *= h
    ans['centr_rect'] = sum_centr_rect
    for i in range(1, n):
        sum_trap += y[i]
    sum_trap = (sum_trap + (math.exp(a) + math.exp(b)) / 2) * h
    ans['trap'] = sum_trap

    return ans


def calculate_int(a, b, ε, meth):
    global k
    n = 2
    int_h = calculate_int_h(a, b, n).get(meth)
    int_h_half = calculate_int_h(a, b, 2 * n).get(meth)
    richardson = (int_h_half - int_h) / (2 ** k - 1)
    while math.fabs(richardson) > ε:
        n *= 2
        int_h = calculate_int_h(a, b, n).get(meth)
        int_h_half = calculate_int_h(a, b, 2 * n).get(meth)
        richardson = (int_h_half - int_h) / (2 ** k - 1)
    meth_error = math.fabs((math.exp(1) - 1) - (int_h_half))
    return "уточненное значение интеграла: " + str(int_h_half) + " для разбиения: " + str(
        n) + " с абсолютной погрешностью: " + ("%.10f" % meth_error)


print(calculate_int_h(0, 1, 2))
print(calculate_int(0, 1, 0.00001, 'trap'))
