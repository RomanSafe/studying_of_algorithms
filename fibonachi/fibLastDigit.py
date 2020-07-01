def fib_digit(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, (b % 10 + a % 10)
    return b % 10


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()