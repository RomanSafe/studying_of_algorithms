def fib(n):
    F = [0 for i in range(0, n + 1)]
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()