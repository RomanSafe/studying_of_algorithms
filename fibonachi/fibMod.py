def fib_mod(n, m):
    a = 0
    b = 1
    c = list()
    while True:
        t = a % m
        if len(c) > 1 and t == 0:
            break
        c.append(t)
        a, b = b, (b + a)
    a = n % len(c)
    
    print(c)
    print("len c", len(c))
    return c[a]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()