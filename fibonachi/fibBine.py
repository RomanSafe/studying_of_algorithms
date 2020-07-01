# Формула Бине

def fib(n):
    return (1 / (5 ** 0.5) * ((((1 + 5 ** 0.5) / 2) ** n) - (((1 - 5 ** 0.5) / 2) ** n)))

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()