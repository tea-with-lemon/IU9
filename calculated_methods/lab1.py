import math

alpha = []
beta = []


def createHelper(a, b, c, d, n):
    global alpha
    global beta
    l = n - 1
    alpha.append(-c[0] / b[0])
    beta.append(d[0] / b[0])
    for i in range(1, l - 1):
        alpha.append(-c[i] / (a[i - 1] * alpha[i - 1] + b[i]))
        beta.append((d[i] - a[i - 1] * beta[i - 1]) / (a[i - 1] * alpha[i - 1] + b[i]))
    return alpha, beta


def createX(a, b, d, n):
    l = n - 1
    global alpha
    global beta
    x = [0 for i in range(0, l)]
    x[l - 1] = (d[l - 1] - a[l - 2] * beta[l - 2]) / (a[l - 2] * alpha[l - 2] + b[l - 1])
    for i in range(l - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]
    return x

#
# def mnk(begin, end):
#     global n
#     x = []
#     y = []
#     h = (end - begin) / n
#     for i in range(0, n):
#         y.append(math.log(math.exp(begin + h * i)))
#         x.append(begin + h * i)
#     A = 0
#     B = 0
#     F = 0
#     D = 0
#     for i in range(0, n):
#         A += x[i] ** 2
#         B += x[i]
#         D += x[i] * y[i]
#         F += y[i]
#     b_star = (F * A - D * B) / (n * A - B ** 2)
#     a_star = (D - B * b_star) / A
#     b = a_star
#     a = math.exp(b_star)
#     return a, b
#
#
# print(mnk(0, 1))
# def calculate_coef(begin, end):
#     global n
#     x = []
#     y = []
#     aind = [0]
#     bind = [0]
#     Dhelp = []
#     dind = [0]
#     Sind = []
#     h = (end - begin) / n
#     for i in range(0, n + 1):
#         y.append(math.exp(begin + h * i))
#         x.append(begin + h * i)
#
#     for i in range(0, n - 1):
#         a.append(1)
#         c.append(1)
#     for i in range(0, n):
#         b.append(4)
#     for i in range(1, n):
#         Dhelp.append((3 / h ** 2) * (y[i - 1] + y[i + 1] - 2 * y[i]))
#     createHelper(Dhelp)
#     cind = [0, 0] + createX(Dhelp) + [0]
#
#     for i in range(1, n + 1):
#         aind.append(y[i - 1])
#     for i in range(1, n + 1):
#         dind.append((cind[i + 1] - cind[i]) / (3 * h))
#     for i in range(1, n + 1):
#         bind.append(((y[i] - y[i - 1]) / h) - (h / 3) * (c[i + 1] + 2 * c[i]))
#         Sind.append(bind[i] + 2 * cind[i] * (x[i] - x[i - 1]) + 3 * dind[i] * (x[i] - x[i - 1]) ** 2)
#     return cind, dind, aind
#
#
# print(calculate_coef(0, 1))
