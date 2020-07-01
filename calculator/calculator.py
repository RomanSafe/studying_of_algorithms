from collections import deque

def calculate_min_of_operations(number):
    intermediate_numbers = {item: [0, 0] for item in range(1, number + 1)}
    if number == 1:
        return (intermediate_numbers[number][0], (number,))
    for item in range(1, number):
        if intermediate_numbers[item + 1][0] == 0:
            intermediate_numbers[item + 1][0] = intermediate_numbers[item][0] + 1
            intermediate_numbers[item + 1][1] = item
        elif intermediate_numbers[item + 1][0] > intermediate_numbers[item][0] + 1:
            intermediate_numbers[item + 1][0] = intermediate_numbers[item][0] + 1
            intermediate_numbers[item + 1][1] = item

        if item * 2 in intermediate_numbers:
            if intermediate_numbers[item * 2][0] == 0:
                intermediate_numbers[item * 2][0] = intermediate_numbers[item][0] + 1
                intermediate_numbers[item * 2][1] = item
            elif intermediate_numbers[item * 2][0] > intermediate_numbers[item][0] + 1:
                intermediate_numbers[item * 2][0] = intermediate_numbers[item][0] + 1
                intermediate_numbers[item * 2][1] = item

        if item * 3 in intermediate_numbers:
            if intermediate_numbers[item * 3][0] == 0:
                intermediate_numbers[item * 3][0] = intermediate_numbers[item][0] + 1
                intermediate_numbers[item * 3][1] = item
            elif intermediate_numbers[item * 3][0] > intermediate_numbers[item][0] + 1:
                intermediate_numbers[item * 3][0] = intermediate_numbers[item][0] + 1
                intermediate_numbers[item * 3][1] = item
    backcount = number
    decision = deque()
    while backcount:
        decision.append(backcount)
        backcount = intermediate_numbers[backcount][1]

    return (intermediate_numbers[number][0], reversed(decision))


def preparation():
    amount_of_operations, decision = calculate_min_of_operations(int(input()))
    print(amount_of_operations)
    for i in decision:
        print(i, end=' ')


if __name__ == '__main__':
    preparation()
