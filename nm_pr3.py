import math

def f(x):
    return -2 * x * math.exp(-x) + math.exp(-2 * x) + x**2

def df(x):
    return -2 * math.exp(-x) + 2 * x * math.exp(-x) - 2 * math.exp(-2 * x) + 2 * x


def newton(x0, f, df, eps, maxit):
    x_varasem= x0
    for i in range(maxit):
        x_uus = x_varasem - f(x_varasem) / df(x_varasem)
        if abs(x_uus - x_varasem) <= eps:
            return x_uus, i+1
        x_varasem = x_uus

    return x_uus, maxit

x0 = 0.0
eps = 1e-5
maxit = 100

lahend, sammud = newton(x0, f, df, eps, maxit)

print(lahend)
print(sammud)  