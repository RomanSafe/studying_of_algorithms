import time
from matplotlib import pyplot as plt
from sympy import limit, ln, symbols, sqrt, diff, exp, log, oo, factorial, Pow, Function, E, exp, Integer, pi, \
    Rational, Float, nan, sympify

n = symbols('n', real=True)


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)
        plt.show()


def f1(n):
    a = log(log(n, 2), 2)
    c = limit(a, n, oo)
    return c


def f2(n):
    b = (log(n, 4)) ** 0.5
    c = limit(b, n, oo)
    return c


if __name__ == '__main__':
    compare([f1], list(range(200)))
    compare([f2], list(range(200)))
