def fib_mod(n, m):
    a, b = 0, 1
    c = [a, b]
    
    while True:
        a, b = b, ((b + a) % m)
        c.append(b)
        
        if c[-2] == 0 and c[-1] == 1:        
            break
    
    return c[n % len(c[:-2])]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()