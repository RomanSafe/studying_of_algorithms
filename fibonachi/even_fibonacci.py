def even_fibonacci(length):
    if length <= 0:
        return None
    result = [0 for _ in range(length)]
    number1, number2 = 0, 1
    pointer = 1
    while pointer < length:
        if number2 % 2 == 0:
            result[pointer] = number2
            pointer += 1
        number1, number2 = number2, number1 + number2
    return result


if __name__ == '__main__':
    print(even_fibonacci(0))

